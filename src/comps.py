import json

def table_row(name, comp, count):
  if "info" in comp.keys():
    return f"""
        <tr>
          <td>{count}</td>
          <td><a href="{comp["url"]}">{name}</a></td>
          <td>{comp["info"]}</td>
        </tr>"""

  else:
    return f"""
        <tr>
          <td>{count}</td>
          <td colspan="2"><a href="{comp["url"]}">{name}</a></td>
        </tr>"""

def table_rows(comps):
  year = list(comps)[0][-4:]
  count = 0
  rows = []

  for x, name in zip(range(len(comps)), comps):
    if name[-4:] != year:
      rows.append(f"""
        <tr>
          <td colspan="3" id="{year}">{count} {"comps" if count > 1 else "comp"} in {year}</td>
        </tr>""")
      year = name[-4:]
      count = 0

    rows.append(table_row(name, comps[name], x + 1))
    count += 1

  rows.append(f"""
        <tr>
          <td colspan="3" id="total">Total: {len(comps)}</td>
        </tr>""")

  return "".join(rows)

def comps_to_table(comps):
  return f"""    <table>
      <thead>
        <tr>
          <th>#</th>
          <th>Name</th>
          <th>Info</th>
        </tr>
      </thead>
      <tbody>""" + table_rows(comps) + f"""
      </tbody>
    </table>"""

def main():
  with open("../docs/comps.json", "r") as comps:
    comps = json.load(comps)

  with open("../docs/comps/index.html", "w") as index:
    index.write(
      f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <title>my comps - RaspBella</title>
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
      <h2>My Comps</h2>
    </div>
{comps_to_table(comps)}
  </body>
</html>""")

if __name__ == "__main__":
  main()
