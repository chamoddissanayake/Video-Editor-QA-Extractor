
def snippetModifierFunc(preSnippet):
    updated_snippet = ""
    updated_snippet = str(preSnippet).strip()

    updated_snippet = updated_snippet.replace('History[edit].', ' ')

    if 'xa0' in updated_snippet:
        updated_snippet = str(updated_snippet.split('xa0')[0]).strip()

    temp = ""
    for i in range(3):
        temp += updated_snippet[i]
    if temp == 'Jan' or temp == 'Feb' or temp == 'Mar' or temp == 'Apr' or temp == 'May' or temp == 'Jun' or temp == 'Jul' or temp == 'Aug' or temp == 'Sep' or temp == 'Oct' or temp == 'Nov' or temp == 'Dec':
        b = ""
        tempSplittedArr = updated_snippet.split('...')
        for i, item in enumerate(tempSplittedArr):
            if i != 0:
                b += item
        updated_snippet = b
    else:
        c = ""
        tempSplittedArr = updated_snippet.split('...')
        for i, item in enumerate(tempSplittedArr):
            c += item
        updated_snippet = c

    # replace \n
    updated_snippet = updated_snippet.replace('\n', ' ')
    updated_snippet = updated_snippet.replace('\t', ' ')

    updated_snippet = updated_snippet.replace("/", "")

    htmltaglist = ['<!--...-->', '<!DOCTYPE>', '<a>', '<abbr>', '<acronym>', '<address>', '<applet>', '<area>',
                   '<article>', '<aside>', '<audio>', '<b>', '<base>', '<basefont>', '<bdi>', '<bdo>', '<big>',
                   '<blockquote>', '<body>', '<br>', '<button>', '<canvas>', '<caption>', '<center>', '<cite>',
                   '<code>', '<col> ', '<colgroup>', '<data>', '<datalist>', '<dd>', '<del>', '<details>', '<dfn>',
                   '<dialog>', '<dir>', '<div>', '<dl>', '<dt>', '<em>', '<embed>', '<fieldset>', '<figcaption>',
                   '<figure>', '<font>', '<footer>', '<form>', '<frame>', '<frameset>', '<h1>', '<h2>', '<h3>', '<h4>',
                   '<h5>', '<h6>', '<head>', '<header>', '<hr>', '<html>', '<i>', '<iframe>', '<img>', '<input>',
                   '<ins>', '<kbd>', '<label>', '<legend>', '<li>', '<link>', '<main>', '<map>', '<mark>', '<meta>',
                   '<meter>', '<nav>', '<noframes>', '<noscript>', '<object>', '<ol>', '<optgroup>', '<option>',
                   '<output>', '<p>', '<param>', '<picture>', '<pre>', '<progress>', '<q>', '<rp>', '<rt>', '<ruby>',
                   '<s>', '<samp>', '<script>', '<section>', '<select>', '<small>', '<source>', '<span>', '<strike>',
                   '<strong>', '<style>', '<sub>', '<summary>', '<sup>', '<svg>', '<table>', '<tbody>', '<td>',
                   '<template>', '<textarea>', '<tfoot>', '<th>', '<thead>', '<time>', '<title>', '<tr>', '<track>',
                   '<tt>', '<u>', '<ul>', '<var>', '<video>', '<wbr>',
                   '</a>', '</abbr>', '</acronym>', '</address>', '</applet>', '</area>', '</article>', '</aside>',
                   '</audio>', '</b>', '</base>', '</basefont>', '</bdi>', '</bdo>', '</big>', '</blockquote>',
                   '</body>', '</br>', '</button>', '</canvas>', '</caption>', '</center>', '</cite>', '</code>',
                   '</col> ', '</colgroup>', '</data>', '</datalist>', '</dd>', '</del>', '</details>', '</dfn>',
                   '</dialog>', '</dir>', '</div>', '</dl>', '</dt>', '</em>', '</embed>', '</fieldset>',
                   '</figcaption>', '</figure>', '</font>', '</footer>', '</form>', '</frame>', '</frameset>', '</h1>',
                   '</h2>', '</h3>', '</h4>', '</h5>', '</h6>', '</head>', '</header>', '</hr>', '</html>', '</i>',
                   '</iframe>', '</img>', '</input>', '</ins>', '</kbd>', '</label>', '</legend>', '</li>', '</link>',
                   '</main>', '</map>', '</mark>', '</meta>', '</meter>', '</nav>', '</noframes>', '</noscript>',
                   '</object>', '</ol>', '</optgroup>', '</option>', '</output>', '</p>', '</param>', '</picture>',
                   '</pre>', '</progress>', '</q>', '</rp>', '</rt>', '</ruby>', '</s>', '</samp>', '</script>',
                   '</section>', '</select>', '</small>', '</source>', '</span>', '</strike>', '</strong>', '</style>',
                   '</sub>', '</summary>', '</sup>', '</svg>', '</table>', '</tbody>', '</td>', '</template>',
                   '</textarea>', '</tfoot>', '</th>', '</thead>', '</time>', '</title>', '</tr>', '</track>', '</tt>',
                   '</u>', '</ul>', '</var>', '</video>', '</wbr>']

    # remove html tags
    for item in htmltaglist:
        updated_snippet = updated_snippet.replace(item, '')


    if "days ago" in updated_snippet:
        for i,item in enumerate(range(30)):
            temp = ""
            temp = str(i) + " days ago"
            if temp in updated_snippet:
                updated_snippet = updated_snippet.replace(temp, '')

    updated_snippet = str(updated_snippet).strip()
    return updated_snippet