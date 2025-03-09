import exp_utils
import time
import cvc5
from exp_parser import get_arg_parser

parser = get_arg_parser()
args = parser.parse_args()

input_file = args.input_file
opts = args.options

partitioner = args.partitioner

# Make partitions
partitioning_start_time = time.time()

# Using climit and checks-before-partition to make deterministic partitions
number_of_partitions = 8
partitioner_options = " --partition-when climit "
partitioning_timeout = 60000
partitions = exp_utils.make_partitions(partitioner=partitioner,
                            partitioner_options=partitioner_options,
                            number_of_partitions=number_of_partitions,
                            smt_file=input_file,
                            checks_before_partition=args.checks_before_partitioning,
                            checks_between_partitions=1,
                            strategy="decision-cube",
                            time_limit=partitioning_timeout
                            )
partitioning_end_time = time.time()
partitioning_time = partitioning_end_time - partitioning_start_time

print(f"Generated partitions {len(partitions)} in {partitioning_time} seconds")
for p in partitions:
    print(p)

# Get the input formula, everything before (check-sat)
# Note: this is not the most efficient way to do this, but it works
with open(input_file, 'r') as f:
    input_formula = f.read()

unsat_core_lemmas = []
unsat_core_assumptions = []

for i in range(len(partitions)):
    p = partitions[i]
    # Set up solver
    slv = cvc5.Solver()
    slv.setOption("incremental", "false")

    # For getting unsat cores etc.
    if args.dump_unsat_cores:
        slv.setOption("produce-unsat-cores", "true")
        slv.setOption("produce-proofs", "true")
        slv.setOption("produce-unsat-assumptions", "true")

    exp_utils.apply_options(slv, exp_utils.strategy_map[opts])
    parser = cvc5.InputParser(slv)

    parser.setStringInput(cvc5.InputLanguage.SMT_LIB_2_6, input_formula, "original")
    sm = parser.getSymbolManager()

    while True:
        cmd = parser.nextCommand()
        if cmd.isNull():
            break
        elif cmd.getCommandName() == "check-sat":
            # insert the partitioning formula before check-sat
            partitioning_formula = f"(assert {p})"
            parser2 = cvc5.InputParser(slv, sm) 
            parser2.setStringInput(cvc5.InputLanguage.SMT_LIB_2_6, partitioning_formula, "partition")
            assert_p = parser2.nextCommand()
            assert_p.invoke(slv, sm)
            partition_solve_start_time = time.time()
            res = slv.checkSat()
            partition_solve_end_time = time.time()
            break
        else:
            cmd.invoke(slv, sm)

    partition_solve_time = partition_solve_end_time - partition_solve_start_time

    stats = slv.getStatistics()
    print(f"P{i} Solve Time: {partition_solve_time}")
    num_conflicts = stats["sat::conflicts"]["value"]
    num_decisions = stats["sat::decisions"]["value"]
    num_resource_units = stats["resource::resourceUnitsUsed"]["value"]
    print(f"P{i} Resources : {num_resource_units}")
    print(f"P{i} Conflicts : {num_conflicts}")
    print(f"P{i} Decisions : {num_decisions}")
    print(f"P{i} Result    : {res}")

    if args.dump_unsat_cores:
        if res.isUnsat():
            if args.dump_file:
                with open(args.dump_file, 'a') as f:
                    f.write(f"Partition {i} unsat core lemmas:\n")
                    for ucl in slv.getUnsatCoreLemmas():
                        f.write(f"{ucl}\n")
            else:
                print(f"Partition {i} unsat core lemmas:\n")
                for ucl in slv.getUnsatCoreLemmas():
                    print(ucl)
        else:
            print("sat or unknown, no unsat core")

    # bonus line to make output a little easier to read
    print()
    
