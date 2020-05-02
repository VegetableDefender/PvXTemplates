# PvXTemplates

A set of scripts to generate some gwpvx templates


## {{Requires-Consumables}}

[PvX Talk](https://gwpvx.gamepedia.com/User_talk:Vegetaledefender/TestPage#Consumables_Template%3A_Types)


### Usage

- Install dependencies with `poetry install`
- Generate the template by running `poetry run python requires_consumables.py`. This will take the data from `consumables.json` and write the template to `requires_consumables.pvx`


#### Data structure

`consumables.json`'s structure is simple:

- The first level keys are parameter categories. Their names will be used as section headers in the PvX page's **Usage** section
- The second level is a list of objects, containing the following keys:
  - `ǹame`*(string)*: Display name of the consumable
  - `file`*(string)*: PvX internal name of the image to be used
  - `params`*(list -> string)*: Parameter(s) that need to be set equal to `yes` in order to select this consumable

