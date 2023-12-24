# rasperry-pi-pico-samizdat
Anonymous, guerrilla publishing with a Raspberry Pi Pico and a library for WLAN Captive portal / Hotspot creation. 

Why the name? 

According to Wikipedia a samizdat is a "self-published work of dissident literature, which was clandestinely distributed in the former Soviet bloc countries."

This project is inspired by an article in C't (a German computer magazine) 23/2033. 

It will turn a Raspberry Pi Pico W into a WLAN Hotspot with a captive portal. The possible uses are many, but the one proposed in the article was to use it for a sort of "Guerilla publishing".  
A Raspberry Pi Pico W is a cheap device, at way under 10$/€ so if you are unable to retrieve your device after the battery has run out or if it gets lost, there win't be a big loss. It can run for a couple of days on an 18650 Li-ion rechargeable battery or on 3 1,5V primary cells. 

A quick summary: 

- A Raspberry Pi Pico creates a WLAN.
- Once a client connects to it, it will set itself as the destination of any DNS requests.
- The index.html page is displayed, both on first connection or on any web request.

Possible uses (legality aside :) ): 

- Informational WLAN in a public location.
- Provide information in case of news and media outages or strict censorship.
- Dead Letter Box (with encrypted content, of course) for intelligence agents.
- Fun and guerrilla way of publishing something. 

Quick Start: 

- Clone this repo.
- Open in Thonny.
- Edit htdocs/index.html to show your desired information.
- Install micrpython-phew library/package to Raspberry Pi Pico W (I use Thonny, makes this quick and easy).
- Copy all files to your Raspberry Pi Pico W.
- Power it up however you like, have fun in your neighborhood or some public place.

