<p align="center">
  <img src=".github/assets/banner.png" alt="Formable Nations: Reworked" width="100%">
</p>

<p align="center">
  <a href="https://github.com/JihadJackass/Formable-Nations-Reworked-EUV/commits/main"><img alt="Mod version" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FJihadJackass%2FFormable-Nations-Reworked-EUV%2Fmain%2F.github%2Fbadges.json&query=%24.mod_version&label=mod%20version&color=c99a3c&style=for-the-badge"></a>
  <img alt="Supported game version" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FJihadJackass%2FFormable-Nations-Reworked-EUV%2Fmain%2F.github%2Fbadges.json&query=%24.game_version&label=EU5&color=1d4f8c&style=for-the-badge">
  <img alt="Checksum" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FJihadJackass%2FFormable-Nations-Reworked-EUV%2Fmain%2F.github%2Fbadges.json&query=%24.checksum&label=checksum&color=555555&style=for-the-badge">
  <img alt="Formable nations" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FJihadJackass%2FFormable-Nations-Reworked-EUV%2Fmain%2F.github%2Fbadges.json&query=%24.formables&label=formable%20nations&color=7a2e2e&style=for-the-badge">
</p>
<p align="center">
  <a href="https://github.com/JihadJackass/Formable-Nations-Reworked-EUV/commits/main"><img alt="Last update" src="https://img.shields.io/github/last-commit/JihadJackass/Formable-Nations-Reworked-EUV?label=last%20update&style=flat-square&color=c99a3c"></a>
  <a href="https://github.com/JihadJackass/Formable-Nations-Reworked-EUV/issues"><img alt="Open issues" src="https://img.shields.io/github/issues/JihadJackass/Formable-Nations-Reworked-EUV?style=flat-square"></a>
  <a href="https://github.com/JihadJackass/Formable-Nations-Reworked-EUV/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/JihadJackass/Formable-Nations-Reworked-EUV?style=flat-square&color=c99a3c"></a>
</p>

**Formable Nations: Reworked** is a complete overhaul of formable nations for *Europa Universalis V*. It adds over 200 new formable nations, reworks every vanilla formable, and gives many of them their own governments, events, disasters and mechanics. Every formable can be switched on or off in-game, so you only play with the ones you want.

---

## Contents

- [Features](#features)
- [Content packs](#content-packs)
- [In-game settings](#in-game-settings)
- [Installation](#installation)
- [Compatibility](#compatibility)
- [Reporting bugs](#reporting-bugs)
- [Controversial version](#controversial-version)

---

## Features

| | |
|---|---|
| **364 formable nations** | 200+ new formables plus all 156 vanilla formables, from historical kingdoms to alt-history empires |
| **Reworked vanilla formables** | Every vanilla and colonial formable reviewed, with fixed requirements and FNR toggles |
| **Unique content** | Custom governments, reforms, laws, estate privileges, advances, units, buildings and international organizations |
| **Events and disasters** | Event chains, flavor and custom disasters for the bigger nations |
| **Full control** | Turn whole categories or single nations on and off in-game, at any time |
| **Better country names** | Cleaner names for formables, with a game rule to use simpler names or vanilla's |

## Content packs

Content packs give a group of formables deep, nation-specific gameplay on top of their formation.

### Pax Romana

The heirs of Rome and the ancient world.

| Nation | Highlights |
|---|---|
| **Roman Empire** | Imperial Dioceses, Legion Loyalty, usurpers, the Crisis of the Third Century, the Foederati and client kingdoms |
| **Roman Republic** | Senate Authority, consular elections, dictators and the road to Empire, the Socii, Roman slavery and the Roman Civil Wars |
| **Eastern Roman Empire** | Pentarchy, Greek Fire, cataphracts, the Varangian Guard and the restored sees |
| **Western Roman Empire** | Foederati loyalty, the Limes, the Concilium Occidentis and the Reconquest |
| **Ptolemaic Kingdom** | Basileus and Pharaoh, the Library of Alexandria, the Nile floods and the League of the Islanders |
| **Magna Graecia** | The Hellenic Revival, a Greek and Italian rivalry, and Basilian monasteries |
| **Trebizond** | Peril, Komnenian marriage pacts, the Silk Road and the Empire in Exile |
| **Latin Empire** | The Partition of Romania, the Barons of Romania and a Greek Catholic rite |
| **Gallic Empire** | Druidic Revival or Imperium Galliarum, and the Celtic League |
| **Pontus, Gothia and Dacia** | Mithridates' heirs, the Goths of the Crimea and Zalmoxian Dacia |

More packs are planned.

## In-game settings

Open the settings from the **Formable Nations** button in the form nation window.

- **Categories**: Historical, Non-Historical, Alt-History, Modern, Controversial, Fantasy, Meme, North American and Vanilla. By default only Historical and Vanilla formables are on.
- **Presets**: Default, Plausible, Everything or Vanilla Only, in one click.
- **Individual list**: force any single formable on or off, with A-Z and category filters.
- Settings apply to every country, including the AI, and can be changed mid-game.

**Game rules** (set before starting a game):

- **Country names**: Default, Simple Names, or Vanilla.

## Installation

**Steam Workshop (recommended):** subscribe to the mod and enable it in the launcher playset.

**Manual:**

1. Download this repository (Code > Download ZIP) or clone it.
2. Put the `Formable Nations Reworked` folder in `Documents/Paradox Interactive/Europa Universalis V/mod/`.
3. Enable it in the launcher playset.

Most content works with an existing save, but starting a new game is recommended after updates.

## Compatibility

FNR mostly adds content in its own files, so it works alongside most mods. A few vanilla files have to be replaced for FNR's systems to work. Any other mod that replaces the same files will conflict, and only the version from whichever mod loads last will be used.

| File | Why FNR replaces it |
|---|---|
| `in_game/common/formable_countries/00_formable_countries.txt` | Every vanilla formable, with FNR's toggles and tweaks |
| `in_game/common/customizable_localization/country_name_construction.txt` | How country names are built (FNR parts are marked) |
| `in_game/common/customizable_localization/country_ranks.txt` | Ruler and rank titles |
| `in_game/gui/form_new_country.gui` | Adds the Formable Nations settings button |
| `in_game/gui/hints_lateralview.gui` | Shows the country flag on FNR hints |
| `main_menu/gui/shared/frontend_templates.gui` | Adds a logo to the main menu |

FNR also replaces the four estate-name localization entries (for formable-specific estate names), so mods that rename estates will conflict.

To run both mods, load FNR after the other mod, or ask either author for a compatibility patch. FNR's files are updated after every game patch.

## Reporting bugs

Open an [issue](https://github.com/JihadJackass/Formable-Nations-Reworked-EUV/issues) with:

- the mod version and game version (shown in the badges above)
- what happened, and what you expected
- your `error.log` from `Documents/Paradox Interactive/Europa Universalis V/logs/`, if possible

## Controversial version

An uncensored version with extra content is available separately:
[Formable Nations: Reworked - Uncensored Version](https://github.com/JihadJackass/Formable-Nations-Reworked-Uncensored-Version)
