#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define OUTPUT_DIR "../docs"

enum {
  e_2x2,
  e_3x3,
  e_4x4,
  e_5x5,
  e_6x6,
  e_7x7,
  e_3BLD,
  e_4BLD,
  e_5BLD,
  e_MBLD,
  e_OH,
  e_SQ1,
  e_Pyra,
  e_Skewb,
  e_Mega,
  e_Clock,
  e_FMC,
  EVENT_COUNT
};

const char *e_names[EVENT_COUNT] = {
  [e_2x2] = "2x2",
  [e_3x3] = "3x3",
  [e_4x4] = "4x4",
  [e_5x5] = "5x5",
  [e_6x6] = "6x6",
  [e_7x7] = "7x7",
  [e_3BLD] = "3x3 Blindfolded",
  [e_4BLD] = "4x4 Blindfolded",
  [e_5BLD] = "5x5 Blindfolded",
  [e_MBLD] = "3x3 Multi-Blind",
  [e_OH] = "3x3 One Handed",
  [e_SQ1] = "Square-1",
  [e_Pyra] = "Pyraminx",
  [e_Skewb] = "Skewb",
  [e_Mega] = "Megaminx",
  [e_Clock] = "Clock",
  [e_FMC] = "3x3 Fewest Moves",
};

struct {
  const char *single;
  const char *average;
} pbs[EVENT_COUNT];

typedef struct {
  const char *name;
  const char *url;
  const char *text;
} comp;

// https://gist.github.com/rexim/b5b0c38f53157037923e7cdd77ce685d
#define da_append(xs, x)                                                       \
  do {                                                                         \
    if ((xs)->count >= (xs)->capacity) {                                       \
      if ((xs)->capacity == 0) (xs)->capacity = 256;                           \
      else (xs)->capacity *= 2;                                                \
      (xs)->items = realloc((xs)->items, (xs)->capacity*sizeof(*(xs)->items)); \
    }                                                                          \
    (xs)->items[(xs)->count++] = (x);                                          \
  } while (0)

struct {
  size_t count;
  size_t capacity;
  comp *items;
} comps;

#define PB(event, format, pb) pbs[event].format = pb;

#define COMP2(NAME, URL) da_append(&comps, ((comp){ .name = NAME, .url = URL, .text = NULL }));
#define COMP3(NAME, URL, TEXT) da_append(&comps, ((comp){ .name = NAME, .url = URL, .text = TEXT }));

#define GET_COMP(_1, _2, _3, NAME, ...) NAME
#define COMP(...) GET_COMP(__VA_ARGS__, COMP3, COMP2)(__VA_ARGS__)

void start_html(FILE *fp) {
  fprintf(
    fp,
    "<!DOCTYPE html>\n"
    "<html lang=\"en\">\n"
    "  <head>\n"
    "    <title>cubing pbs - RaspBella</title>\n"
    "    <link rel=\"stylesheet\" href=\"/main.css\">\n"
    "    <meta charset=\"UTF-8\">\n"
    "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
    "    <link rel=\"apple-touch-icon\" sizes=\"180x180\" href=\"/favicon/apple-touch-icon.png\">\n"
    "    <link rel=\"icon\" type=\"image/png\" sizes=\"32x32\" href=\"/favicon/favicon-32x32.png\">\n"
    "    <link rel=\"icon\" type=\"image/png\" sizes=\"16x16\" href=\"/favicon/favicon-16x16.png\">\n"
    "    <link rel=\"manifest\" href=\"/favicon/site.webmanifest\">\n"
    "  </head>\n"
    "  <body>\n"
    "    <ul class=\"nav\">\n"
    "      <li><a href=\"/\">home</a></li>\n"
    "      <li><a href=\"/RaspBella\">about</a></li>\n"
    "      <li><a class=\"active\" href=\"/cubing\">cubing</a></li>\n"
    "      <li><a href=\"/linux\">linux</a></li>\n"
    "      <li><a href=\"/media\">media</a></li>\n"
    "      <li><a href=\"/trans\">transportation</a></li>\n"
    "    </ul>\n"
  );
}

void end_html(FILE *fp) {
  fprintf(
    fp,
    "  </body>\n"
    "</html>"
  );
}

void mbld2html(FILE *fp, const char *pb) {
  fprintf(
    fp,
    "        <tr>\n"
    "          <td>%s</td>\n"
    "          <td colspan=\"2\">%s</td>\n"
    "        </tr>\n",
    e_names[e_MBLD],
    pb
  );
}

void other_event2html(FILE *fp, const char *event, const char *single, const char *average) {
  fprintf(
    fp,
    "        <tr>\n"
    "          <td>%s</td>\n"
    "          <td>%s</td>\n"
    "          <td>%s</td>\n"
    "        </tr>\n",
    event,
    single,
    average
  );
}

void pbs2html(FILE *fp) {
  start_html(fp);

  fprintf(
    fp,
    "    <div>\n"
    "      <h2>Cubing PBs</h2>\n"
    "      <table>\n"
    "        <tr>\n"
    "          <th>Event</th>\n"
    "          <th>PB Single</th>\n"
    "          <th>PB Average <a href=\"/cubing/pbs#average\">(1)<a/></th>\n"
    "        </tr>\n"
  );

  for (int i = 0; i < e_MBLD; i++) {
    other_event2html(fp, e_names[i], pbs[i].single, pbs[i].average);
  }

  mbld2html(fp, pbs[e_MBLD].single);

  for (int i = e_MBLD + 1; i < EVENT_COUNT; i++) {
    other_event2html(fp, e_names[i], pbs[i].single, pbs[i].average);
  }

  fprintf(
    fp,
    "    </table>\n"
    "    <a id=\"average\"><p style=\"margin: 1em;\" id=\"average\">Multi-Blind is the only event with no average/mean format</p></a>\n"
    "    </div>\n"
  );

  end_html(fp);
}

void mbld2json(FILE *fp, const char *pb) {
  fprintf(
    fp,
    "  \"%s\": \"%s\"",
    e_names[e_MBLD],
    pb
  );
}

void other_event2json(FILE *fp, const char *event, const char *single, const char *average) {
  fprintf(
    fp,
    "  \"%s\": {\n"
    "    \"single\": \"%s\",\n"
    "    \"average\": \"%s\"\n"
    "  }",
    event,
    single,
    average
  );
}

void pbs2json(FILE *fp) {
  fprintf(
    fp,
    "{\n"
  );

  other_event2json(fp, e_names[0], pbs[0].single, pbs[0].average);

  for (int i = 1; i < e_MBLD; i++) {
    fprintf(fp, ",\n");

    other_event2json(fp, e_names[i], pbs[i].single, pbs[i].average);
  }

  fprintf(fp, ",\n");

  mbld2json(fp, pbs[e_MBLD].single);

  for (int i = e_MBLD + 1; i < EVENT_COUNT - 1; i++) {
    fprintf(fp, ",\n");

    other_event2json(fp, e_names[i], pbs[i].single, pbs[i].average);
  }

  fprintf(
    fp,
    "\n}"
  );
}

void comp2html(FILE *fp, size_t n, comp comp) {
  if (comp.text) {
    fprintf(
      fp,
      "        <tr>\n"
      "          <td>%zu</td>\n"
      "          <td><a href=\"%s\">%s</a></td>\n"
      "          <td>%s</td>\n"
      "        </tr>\n",
      n,
      comp.url, comp.name,
      comp.text
    );
  }

  else {
    fprintf(
      fp,
      "        <tr>\n"
      "          <td>%zu</td>\n"
      "          <td colspan=\"2\"><a href=\"%s\">%s</a></td>\n"
      "        </tr>\n",
      n,
      comp.url, comp.name
    );
  }
}

void comps2html(FILE *fp) {
  start_html(fp);

  fprintf(
    fp,
    "    <div>\n"
    "      <h2>My Comps</h2>\n"
    "      <table>\n"
    "        <tr>\n"
    "          <th>#</th>\n"
    "          <th>Name</th>\n"
    "          <th>Info</th>\n"
    "        </tr>\n"
  );

  size_t count = 0;
  size_t year_count = 0;

  char y[4] = {
    [0] = comps.items->name[strlen(comps.items->name) - 4],
    [1] = comps.items->name[strlen(comps.items->name) - 3],
    [2] = comps.items->name[strlen(comps.items->name) - 2],
    [3] = comps.items->name[strlen(comps.items->name) - 1]
  };

  for (size_t i = 0; i < comps.count; i++) {
    char ny[4] = {
      [0] = comps.items[i].name[strlen(comps.items[i].name) - 4],
      [1] = comps.items[i].name[strlen(comps.items[i].name) - 3],
      [2] = comps.items[i].name[strlen(comps.items[i].name) - 2],
      [3] = comps.items[i].name[strlen(comps.items[i].name) - 1]
    };

    if (ny[3] != y[3] || ny[2] != y[2] || ny[1] != y[1] || ny[0] != y[0]) {
      fprintf(
        fp,
        "        <tr>\n"
        "          <td colspan=\"3\">%c%c%c%c: %zu/%zu</td>\n"
        "        </tr>\n",
        y[0], y[1], y[2], y[3], year_count, count
      );

      y[0] = ny[0];
      y[1] = ny[1];
      y[2] = ny[2];
      y[3] = ny[3];

      year_count = 0;
    }

    comp2html(fp, i + 1, comps.items[i]);

    count++;
    year_count++;
  }

  fprintf(
    fp,
    "        <tr>\n"
    "          <td colspan=\"3\">%c%c%c%c: %zu/%zu</td>\n"
    "        </tr>\n"
    "      </table>\n"
    "    </div>\n",
    y[0], y[1], y[2], y[3], year_count, count
  );

  end_html(fp);
}

void comp2json(FILE *fp, comp comp) {
  if (comp.text) {
    fprintf(
      fp,
      "  \"%s\": {\n"
      "    \"url\": \"%s\",\n"
      "    \"info\": \"%s\"\n"
      "  }",
      comp.name,
      comp.url,
      comp.text
    );
  }

  else {
    fprintf(
      fp,
      "  \"%s\": {\n"
      "    \"url\": \"%s\"\n"
      "  }",
      comp.name,
      comp.url
    );
  }
}

void comps2json(FILE *fp) {
  fprintf(
    fp,
    "{\n"
  );

  comp2json(fp, *comps.items);

  for (size_t i = 1; i < comps.count; i++) {
    fprintf(
      fp,
      ",\n"
    );

    comp2json(fp, comps.items[i]);
  }

  fprintf(
    fp,
    "\n}"
  );
}

int main(void) {
#include "pbs.c"
#include "comps.c"

  FILE *fp = fopen(OUTPUT_DIR "/pbs/index.html", "w");

  pbs2html(fp);

  fp = freopen(OUTPUT_DIR "/pbs.json", "w", fp);

  pbs2json(fp);

  fp = freopen(OUTPUT_DIR "/comps/index.html", "w", fp);

  comps2html(fp);

  fp = freopen(OUTPUT_DIR "/comps.json", "w", fp);

  comps2json(fp);

  fclose(fp);

  if (comps.count) free(comps.items);
}
