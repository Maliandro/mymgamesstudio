---
title: "Bolt & Breath: Why I Wanted to Ride a Dragon"
seo_title: "Dragon Flying Game for iPhone: Why I Built Bolt & Breath"
slug: bolt-and-breath
description: "I wanted to ride a dragon, so I built a dragon flying game in Unity. The story of Bolt & Breath: Last Dragon, the sea that fought back, and what's next."
date: 2026-10-16
order: 6
cover: img/bolt-and-breath.jpg
keywords: dragon flying game, dragon game iphone, dragon simulator ios, burn the fleet dragon game, ballista shooter, Unity indie game, solo game development
cta_label: Get Bolt & Breath on the App Store
cta_url: https://apps.apple.com/app/id6804506347
---

I'll admit the origin plainly: I'm a Game of Thrones fan, and a Khaleesi fan in particular. Every time she climbed onto a dragon I thought the same thing: I want to do that. Not watch it. Do it.

Bolt & Breath: Last Dragon, my dragon flying game for iPhone, is me, years later, finally building that feeling for myself. Nothing in it comes from the show; it's my own world and my own story. But that wish is where it started.

## What the game is: fly, burn the fleet, man the ballista

You are the last dragon. A royal fleet and its castles stand between you and whatever comes next, and your job is to burn them. You fly low over the water, line up a ship, breathe fire and watch the sails catch. Then you bank and come around for the next one.

In between, you switch sides. Short ballista sections put you on the ground as a shooter, aiming heavy bolts at a dragon coming for you. It felt right that a game about being the dragon should also let you feel what it's like to face one. The name comes from those two halves: bolt and breath.

There's also a free-flight island for when you just want to fly, and ten dragons to unlock over time.

## How weak the first versions were

I want to be honest about this because the clips I post now don't show it. The first builds were bad. The dragon floated like a paper plane. The fire came out of the wrong place. The sea was a flat blue sheet. Castles looked like boxes. I had a feeling I wanted and almost nothing on screen that delivered it.

I built it in Unity, learning as I went, on a laptop with integrated graphics. That last detail shaped everything. If it ran badly for me, it would run badly on a phone, so I had to find cheap tricks for things big studios solve with raw power.

## The sea

The water took longer than anything else, and it never quite stopped fighting me. A dragon game over the ocean is mostly ocean; if the sea looks wrong, nothing else matters.

At one point the water in the hub had a strange checkerboard pattern that I was sure came from the cloud shadows. I spent two full rounds of fixes blaming the clouds. It was the waves: I was calculating their slope at the vertices, and at the grid size I was using, the wave length and the grid lined up badly and produced a moiré pattern. Moving that calculation to per-pixel fixed it in an evening, after days spent in the wrong place. I think about that often. The bug is rarely where you're angriest.

Then the night sea, foam that wouldn't stop, brightness that looked different on every phone. Each update has touched the water, and the next one probably will too.

## The dragon: flight feel, fire and look

The second hardest thing was the dragon itself, in three ways.

**Flight feel.** Turning too fast felt like a toy; too slow felt like a bus. Getting a creature that heavy to feel responsive took many small adjustments to speed, banking and how the camera follows.

**Fire.** For a while the flame started from the wrong bone and appeared beside the head instead of from the mouth. Then a particle shader variant was stripped out of the iOS build and the fire rendered as black squares on real devices while looking fine in the editor. Every fix like that teaches you a new place to look.

**Look.** Making a dragon read as a dragon — scale, wing movement, how light hits it — on hardware that can't afford much is a constant trade, and I'm still making it.

## Where it is now

Bolt & Breath: Last Dragon has been on the App Store since September 2026, and I've shipped updates every week or two since: fire from the mouth, ships that catch properly, a darker night, tilt controls, towers that collapse when they burn. Version 1.4.0 just went live. There's a long list still, and I'm not done. I still think of that first floaty paper-plane dragon every time I open the project, and it's still the game I most want to get right.
