import exp_utils
import time
import cvc5
from exp_parser import get_arg_parser

parser = get_arg_parser()
args = parser.parse_args()

input_file = args.input_file
opts = args.options

# Set up the solver
slv = cvc5.Solver()
slv.setOption("incremental", "false")

if args.dump_unsat_cores:
    slv.setOption("produce-unsat-cores", "true")
    slv.setOption("produce-proofs", "true")
    slv.setOption("produce-unsat-assumptions", "true")

exp_utils.apply_options(slv, exp_utils.strategy_map[opts])
cvc5_parser = cvc5.InputParser(slv)
cvc5_parser.setFileInput(cvc5.InputLanguage.SMT_LIB_2_6, input_file)
sm = cvc5_parser.getSymbolManager()

# Parse the file
while True:
    cmd = cvc5_parser.nextCommand()
    if cmd.isNull():
        break
    elif cmd.getCommandName() == "check-sat":
        
        # Time check-sat
        solve_time_start = time.time()
        res = slv.checkSat()
        solve_time_end = time.time()
        solve_time = solve_time_end - solve_time_start

        # Get stats and dump info
        stats = slv.getStatistics()
        
        print(f"Solve Time: {solve_time}")
        num_conflicts = stats["sat::conflicts"]["value"]
        num_decisions = stats["sat::decisions"]["value"]
        num_resource_units = stats["resource::resourceUnitsUsed"]["value"]
        print(f"Resources : {num_resource_units}")
        print(f"Conflicts : {num_conflicts}")
        print(f"Decisions : {num_decisions}")
        print(f"Result    : {res}")

        if args.dump_unsat_cores:
            if res.isUnsat():
                if args.dump_file:
                    with open(args.dump_file, 'w') as f:
                        f.write(f"unsat core lemmas:\n")
                        for ucl in slv.getUnsatCoreLemmas():
                            f.write(f"{ucl}\n")
                else:
                    print(f"unsat core lemmas:\n")
                    for ucl in slv.getUnsatCoreLemmas():
                        print(ucl)
            else:
                print("sat or unknown, no unsat core")

        break
    else:
        cmd.invoke(slv, sm)