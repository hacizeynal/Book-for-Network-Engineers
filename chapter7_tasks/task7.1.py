output = "\n{:25} {}" * 5

with open("ospf.txt") as ospf_output:
    for lines in ospf_output:
        route = lines.replace("[", "").replace("]", "").replace(",", "")
        route = route.split()
        print(output.format("Prefix", route [1],
                            "AD/Metric",route[2],
                            "Next-hop",route[4],
                            "Last Update",route[5],
                            "Outbound Interface",route[6]))
