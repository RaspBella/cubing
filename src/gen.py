import json

def main():
  with open("../docs/pbs.json", "r") as pbs:
    pbs = json.load(pbs)

  with open("template.html", "r") as t:
    t = t.read()

  with open("../docs/pbs/index.html", "w") as i:
    i.write(t.format(
      pbs["2x2"]["single"],
      pbs["2x2"]["average"],
      pbs["3x3"]["single"],
      pbs["3x3"]["average"],
      pbs["4x4"]["single"],
      pbs["4x4"]["average"],
      pbs["5x5"]["single"],
      pbs["5x5"]["average"],
      pbs["6x6"]["single"],
      pbs["6x6"]["average"],
      pbs["7x7"]["single"],
      pbs["7x7"]["average"],
      pbs["3bld"]["single"],
      pbs["3bld"]["average"],
      pbs["4bld"]["single"],
      pbs["4bld"]["average"],
      pbs["5bld"]["single"],
      pbs["5bld"]["average"],
      pbs["mbld"],
      pbs["oh"]["single"],
      pbs["oh"]["average"],
      pbs["sq1"]["single"],
      pbs["sq1"]["average"],
      pbs["pyra"]["single"],
      pbs["pyra"]["average"],
      pbs["skewb"]["single"],
      pbs["skewb"]["average"],
      pbs["mega"]["single"],
      pbs["mega"]["average"],
      pbs["clock"]["single"],
      pbs["clock"]["average"],
      pbs["fmc"]["single"],
      pbs["fmc"]["average"],
    ))

if __name__ == "__main__":
  main()
