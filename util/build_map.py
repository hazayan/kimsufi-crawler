#!/usr/bin/env python3
import json
from lxml.html.soupparser import parse

def build_map():
    doc = parse("serveurs.xml")
    m = {}
    for e in doc.xpath("//tr[@class='zone-dedicated-availability']"):
        key = e.get("data-ref")
        name = e.xpath(f"//tr[@data-ref='{key}']/td/span[@class='blue fw800']/text()")[0]
        m[key] = name
    sorted(m)
    print(json.dumps(m, indent = 4))

build_map()
