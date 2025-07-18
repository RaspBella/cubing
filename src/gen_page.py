def insert(text, pbs):
    text = text.replace('insert-2x2-single', pbs['2x2']['single'])
    text = text.replace('insert-2x2-average', pbs['2x2']['average'])
    text = text.replace('insert-3x3-single', pbs['3x3']['single'])
    text = text.replace('insert-3x3-average', pbs['3x3']['average'])
    text = text.replace('insert-4x4-single', pbs['4x4']['single'])
    text = text.replace('insert-4x4-average', pbs['4x4']['average'])
    text = text.replace('insert-5x5-single', pbs['5x5']['single'])
    text = text.replace('insert-5x5-average', pbs['5x5']['average'])
    text = text.replace('insert-6x6-single', pbs['6x6']['single'])
    text = text.replace('insert-6x6-average', pbs['6x6']['average'])
    text = text.replace('insert-7x7-single', pbs['7x7']['single'])
    text = text.replace('insert-7x7-average', pbs['7x7']['average'])
    text = text.replace('insert-3bld-single', pbs['3bld']['single'])
    text = text.replace('insert-3bld-average', pbs['3bld']['average'])
    text = text.replace('insert-4bld-single', pbs['4bld']['single'])
    text = text.replace('insert-4bld-average', pbs['4bld']['average'])
    text = text.replace('insert-5bld-single', pbs['5bld']['single'])
    text = text.replace('insert-5bld-average', pbs['5bld']['average'])
    text = text.replace('insert-mbld', pbs['mbld'])
    text = text.replace('insert-oh-single', pbs['oh']['single'])
    text = text.replace('insert-oh-average', pbs['oh']['average'])
    text = text.replace('insert-sq1-single', pbs['sq1']['single'])
    text = text.replace('insert-sq1-average', pbs['sq1']['average'])
    text = text.replace('insert-pyra-single', pbs['pyra']['single'])
    text = text.replace('insert-pyra-average', pbs['pyra']['average'])
    text = text.replace('insert-skewb-single', pbs['skewb']['single'])
    text = text.replace('insert-skewb-average', pbs['skewb']['average'])
    text = text.replace('insert-mega-single', pbs['mega']['single'])
    text = text.replace('insert-mega-average', pbs['mega']['average'])
    text = text.replace('insert-clock-single', pbs['clock']['single'])
    text = text.replace('insert-clock-average', pbs['clock']['average'])
    text = text.replace('insert-fmc-single', pbs['fmc']['single'])
    text = text.replace('insert-fmc-average', pbs['fmc']['average'])

    return text

def main():
    import json

    f = open('../docs/pbs.json', 'r')
    pbs = json.load(f)
    f.close()

    f = open('../docs/pbs/index.html', 'w')
    t = open('template.html', 'r')

    f.write(insert(t.read(), pbs))

    f.close()
    t.close()

if __name__ == '__main__':
    main()
