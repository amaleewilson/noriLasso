import subprocess

# Different strategies for running QF_LRA problems
strategy_map = {
                "default" : [],

                "stoponly" : [("decision", "stoponly")],

                "libtrickstoponly" : [("miplib-trick", "true"), ("miplib-trick-subs", "4"), ("use-approx", "true"), 
                ("lemmas-on-replay-failure", "true"), ("replay-early-close-depth", "4"),
                ("replay-lemma-reject-cut", "128"), ("replay-reject-cut", "512"),
                ("unconstrained-simp", "true"), ("use-soi", "true"), ("decision", "stoponly")],

                "restrictstoponly" : [("restrict-pivots", "false"), ("use-soi", "true"), ("new-prop", "true"), 
                ("unconstrained-simp", "true"), ("decision", "stoponly")],


                "internal" : [("decision", "internal")],

                "libtrickinternal" : [("miplib-trick", "true"), ("miplib-trick-subs", "4"), ("use-approx", "true"), 
                ("lemmas-on-replay-failure", "true"), ("replay-early-close-depth", "4"),
                ("replay-lemma-reject-cut", "128"), ("replay-reject-cut", "512"),
                ("unconstrained-simp", "true"), ("use-soi", "true"), ("decision", "internal")],

                "restrictinternal" : [("restrict-pivots", "false"), ("use-soi", "true"), ("new-prop", "true"), 
                ("unconstrained-simp", "true"), ("decision", "internal")],


                "justif" : [("decision", "justification")],

                "libtrickjustif" : [("miplib-trick", "true"), ("miplib-trick-subs", "4"), ("use-approx", "true"), 
                ("lemmas-on-replay-failure", "true"), ("replay-early-close-depth", "4"),
                ("replay-lemma-reject-cut", "128"), ("replay-reject-cut", "512"),
                ("unconstrained-simp", "true"), ("use-soi", "true"), ("decision", "justification")],

                "restrictjustif" : [("restrict-pivots", "false"), ("use-soi", "true"), ("new-prop", "true"), 
                ("unconstrained-simp", "true"), ("decision", "justification")]
    }

def apply_options(solver, strategy):
    for spair in strategy:
        solver.setOption(spair[0], spair[1])

def make_partitions(partitioner, partitioner_options, number_of_partitions,
                    smt_file, checks_before_partition, checks_between_partitions,
                    strategy, time_limit):

    # Build the partition command
    partition_command = (
        f"{partitioner} --compute-partitions={number_of_partitions} "
        f" --tlimit={time_limit} "
        f"--lang=smt2 --partition-strategy={strategy} "
        f"--checks-before-partition={checks_before_partition} "
        f"--checks-between-partitions={checks_between_partitions} "
        f"{partitioner_options} {smt_file}"
    )

    try:
        output = subprocess.check_output(
            partition_command, shell=True, stderr=subprocess.STDOUT)
        partitions = output.decode("utf-8").strip().split('\n')


        # Handle case where problem is solved while partitioning.
        if partitions[-1] == "sat":
            return "sat"
        elif len(partitions) == 1 and partitions[-1] == "unsat":
            return "unsat"
        elif len(partitions) == 1 and partitions[-1] == "unknown":
            return "unknown"
        # If not solved, then return the partitions
        else:
            return partitions[0: len(partitions) - 1]
    except Exception as e:
        # If the partitioning timed out, good to know.
        if "timeout" in str(e.output):
            print("timout")
            return "timeout"
        # Any other error is just an error.
        else:
            print(e)
            return "error"
