import pdb
import pprint

import sys

import lxml.etree as etree


#-file = sys.argv[1]

file = 'sampletickets.xml'
xobj = etree.parse(file)

tickets = xobj.xpath('//ticket')

x = tickets[0]

x_at = x.xpath('assigned-at')

# these are equivalent
ct_1 = xobj.xpath('/tickets/ticket/current-tags')
ct_2 = xobj.xpath('//current-tags')
ct_2_0_parent = ct_2[0].xpath('..')[0]  # walk up to the parent
ct_3 = xobj.xpath('/*/*/current-tags')


# pulling out information  ----------------------------------------- #

gimme = ['current-tags', 'description', 'due-date']

top_store = []
for el in xobj.xpath('/tickets/ticket'):
    store = []
    for nd in gimme:    
        val = el.xpath(nd)
        store.append(val[0].text)
    top_store.append(store)

pprint.pprint(top_store)

pdb.set_trace()

# see structure of xobj -- e.g. the XML data parsed into a entree object
# print etree.tostring(xobj)

# see the structure of a particular ticket element -- vary index to vary element 
# ----------------------------------------- #
# print etree.tostring(xobj.xpath('/tickets/ticket')[0])


top_store_dct_l = []
for el in xobj.xpath('/tickets/ticket'):
    store_dct = {}
    for nd in gimme:    
        val = el.xpath(nd)
        store_dct[nd] = val[0].text
    top_store_dct_l.append(store_dct)

pdb.set_trace()

# pulling out even less information ----------------------------------------- #

hello = ['current-tags', 'description']

top_store = []
for el in xobj.xpath('/tickets/ticket'):
    store = []
    for nd in hello:    
        val = el.xpath(nd)
        store.append(val[0].text)
    top_store.append(store)

pprint.pprint(top_store)

pdb.set_trace()
