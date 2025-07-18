def main():
    import os
    import sys
    import json

    filename = os.path.join(os.path.dirname(__file__), '../docs/pbs.json')

    fp = open(filename, 'r')
    pbs = json.load(fp)
    fp.close()



    # edit pbs
    events = list(pbs.keys())

    while True:
        line = input('Event: ').lower()

        if line == '':
            break

        elif line not in events:
            continue

        else:
            event = line

            if event == 'mbld':
                pbs['mbld'] = input(f'{event} pb: ').lower()

            else:
                options = ['single', 'average']

                line = input('(s)ingle/(a)verage: ').lower()

                if line == 's':
                    line = 'single'

                if line == 'a':
                    line = 'average'

                if line == '':
                    continue

                elif line not in options:
                    continue

                else:
                    t = line
                    pbs[event][t] = input(f'{event} pb {t}: ').lower()
                


    fp = open(filename, 'w')
    json.dump(pbs, fp)
    fp.close()

if __name__ == '__main__':
    main()
