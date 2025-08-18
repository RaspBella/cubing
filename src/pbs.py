import json

def main():
  with open("../docs/pbs.json", "r") as pbs:
    pbs = json.load(pbs)

  with open("../docs/pbs/index.html", "w") as index:
    index.write(
      f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <title>cubing pbs - RaspBella</title>
    <link rel="stylesheet" href="/main.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="apple-touch-icon" sizes="180x180" href="/favicon/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon/favicon-16x16.png">
    <link rel="manifest" href="/favicon/site.webmanifest">
  </head>
  <body>
    <ul class="nav">
      <li><a href="/">home</a></li>
      <li><a href="/RaspBella">about</a></li>
      <li><a class="active" href="/cubing">cubing</a></li>
      <li><a href="/linux">linux</a></li>
      <li><a href="/media">media</a></li>
      <li><a href="/trans">transportation</a></li>
    </ul>
    <div>
      <h2>Cubing PBs</h2>
    </div>
    <table>
      <tr>
        <th>Event</th>
        <th>PB Single</th>
        <th>PB Average <a href="/cubing/pbs#average">(1)<a/></th>
      </tr>
      <tr>
        <td>2x2</td>
        <td>{pbs["2x2"]["single"]}</td>
        <td>{pbs["2x2"]["average"]}</td>
      </tr>
      <tr>
        <td>3x3</td>
        <td>{pbs["3x3"]["single"]}</td>
        <td>{pbs["3x3"]["average"]}</td>
      </tr>
      <tr>
        <td>4x4</td>
        <td>{pbs["4x4"]["single"]}</td>
        <td>{pbs["4x4"]["average"]}</td>
      </tr>
      <tr>
        <td>5x5</td>
        <td>{pbs["5x5"]["single"]}</td>
        <td>{pbs["5x5"]["average"]}</td>
      </tr>
      <tr>
        <td>6x6</td>
        <td>{pbs["6x6"]["single"]}</td>
        <td>{pbs["6x6"]["average"]}</td>
      </tr>
      <tr>
        <td>7x7</td>
        <td>{pbs["7x7"]["single"]}</td>
        <td>{pbs["7x7"]["average"]}</td>
      </tr>
      <tr>
        <td>3x3 Blindfolded</td>
        <td>{pbs["3bld"]["single"]}</td>
        <td>{pbs["3bld"]["average"]}</td>
      </tr>
      <tr>
        <td>4x4 Blindfolded</td>
        <td>{pbs["4bld"]["single"]}</td>
        <td>{pbs["4bld"]["average"]}</td>
      </tr>
      <tr>
        <td>5x5 Blindfolded</td>
        <td>{pbs["5bld"]["single"]}</td>
        <td>{pbs["5bld"]["average"]}</td>
      </tr>
      <tr>
        <td>Muli-Blind</td>
	<td colspan="2">{pbs["mbld"]}</td>
      </tr>
      <tr>
        <td>3x3 One-Handed</td>
        <td>{pbs["oh"]["single"]}</td>
        <td>{pbs["oh"]["average"]}</td>
      </tr>
      <tr>
        <td>Square-1</td>
        <td>{pbs["sq1"]["single"]}</td>
        <td>{pbs["sq1"]["average"]}</td>
      </tr>
      <tr>
        <td>Pyraminx</td>
        <td>{pbs["pyra"]["single"]}</td>
        <td>{pbs["pyra"]["average"]}</td>
      </tr>
      <tr>
        <td>Skewb</td>
        <td>{pbs["skewb"]["single"]}</td>
        <td>{pbs["skewb"]["average"]}</td>
      </tr>
      <tr>
        <td>Megaminx</td>
        <td>{pbs["mega"]["single"]}</td>
        <td>{pbs["mega"]["average"]}</td>
      </tr>
      <tr>
        <td>Clock</td>
        <td>{pbs["clock"]["single"]}</td>
        <td>{pbs["clock"]["average"]}</td>
      </tr>
      <tr>
        <td>FMC</td>
        <td>{pbs["fmc"]["single"]}</td>
        <td>{pbs["fmc"]["average"]}</td>
      </tr>
    </table>
    <a id="average"><p style="margin: 1em;" id="average">Multi-Blind is the only event with no average/mean format</p></a>
  </body>
</html>""")

if __name__ == "__main__":
  main()
