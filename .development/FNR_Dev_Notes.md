# Formable Nations: Reworked - Dev Notes

Everything that used to be spread across the dev folder, in one place:

1. Release notes: 3.1.0 "Tokay"
2. Backlog: my own TODOs
3. Community requests
4. Tooling: existing devtools and planned tools
5. Parked code: scripts to update later

Great Moravia's full design spec is in its own file, `Great_Moravia_Design.md`.

---

## 1. Release notes: 3.1.0 "Tokay"

*Named after my favorite gecko species.*

### Additions

**New formables**
- Baden-Alsace
- Baden-Wurttemberg
- Magna Graecia
- Kingdom of Swabia (vanilla has a rank 2 Swabia; this is the upgrade)
- Felvidek (North Hungary)
- Hephthalite Empire / White Huns
- Zapadoslavia
- Great Scotia (includes 1 new reform)
- Federal Republic of Central America
- Gran Columbia
- Babylon
- Serene Republic of Australia
- Assyria
- Assyrian Empire (includes unique location renames; I tried to make them dynamic, but that seems unsupported or broken at the moment)
- First Mexican Empire
- Brandenburg-Prussia
- Poland-Hungary (supports conquest and personal union routes)
- Hungary-Romania (supports conquest and personal union routes)
- Brunei Darussalam
- Philippines (native variant)
- Beta Israel
- Sassanids
- North German Confederation
- South German Confederation
- Elbian Federation (includes unique reforms, privileges and special units)
- Hyperborea
- Austro-Hungarian Empire (includes 2 new reforms)
- Tarraconensis (meant for the Gallic Empire, but can be formed without Gallia)
- Britannia (meant for the Gallic Empire, but can be formed without Gallia)
- Papal HRE: the Papal States can form it by conquering 70% of the existing HRE. It is a papacy-dominated HRE that can launch crusades and establish Holy Kingdoms, and the player can change its name and flag in several ways.

**US states**
- Alabama
- Arkansas
- California
- Cascadia
- Florida
- Georgia
- Iowa
- Kentucky
- Louisiana
- Maryland
- Michigan
- Missouri
- New Jersey
- Ohio
- Oklahoma
- Oregon
- Pennsylvania
- South Carolina
- Tennessee
- Texas
- Virginia
- Washington
- West Virginia
- Wisconsin
- Wyoming

**Nation content**
- Carolingian Empire: 1 reform
- Austrian Empire: 3 advances
- British Empire: 5 government reforms
- Hanseatic League:
  - 5 privileges
  - 4 reforms
  - unique content for dealing with the existing Hansa
- Great Moravia:
  - 1 advance
  - reforms (TODO)
  - unique succession law (Moravian Meritocratic Succession)
  - unique IO (Moravian Patriarchate)
  - a few new modifiers
- Grouped government reforms for Hungary, Slovakia and Great Moravia
- Unique events for:
  - Austria-Hungary
  - Gallic Empire
  - Great Moravia
  - Sorbic Kingdom
  - North German Confederation
  - Papacy

**Cultures and languages**
- Cultures: Semitic and Gallo-Roman
- Languages: Akkadian and Gaulish
- Unique estate names for Lusitania

### Adjustments
- Northumbria
- Latin Empire
- Ducal Prussia
- Prussia
- Hanseatic League
- Philippines (colonial variants)
- Macedonian Empire (includes unique location renames)
- Pontus
- Austrian Empire
- German Empire
- Wendish Empire
- Omani Empire (includes content that helps it acquire its historical colonial empire)
- Gallic Empire (significant content additions and adjustments)
- Jagiellonian Empire
- Umayyads
- Dual Monarchy
- British Empire
- Greater German Reich: moved from rank 5 to rank 6
- Empire of China

### Removals
- Replaced vanilla Jerusalem with an improved FNR variant (still a lot to do)
- Replaced vanilla Galicia-Lodomeria with an improved FNR variant (needs adjustment)

### Fixes
- Netherlands now correctly switches to a republic government
- Various other fixes

---

## 2. Backlog: my own TODOs

### General (carried over from after 2.5.0)
- [ ] Improve how country names are built. Add a setting to switch between simple and non-simple names.
- [ ] Tone down flags that are too bright (there are many).

### Unfinished items from 3.1.0
- [ ] Great Moravia reforms (spec is in `Great_Moravia_Design.md`)
- [ ] FNR Jerusalem: lots still to do
- [ ] FNR Galicia-Lodomeria: needs adjustment
- [ ] Assyrian Empire location renames: make them dynamic if the engine ever supports it
- [ ] Bactrian Synod restoration events: see section 5

### Personal
- [ ] Iberian Wedding

---

## 3. Community requests

### Formables

| Request | Notes | Status |
|---|---|---|
| All 50 US states | | Partly done: 25 states plus Cascadia in 3.1.0 |
| Baden-Wurttemberg | | Done in 3.1.0 |
| Kaiserredux formables | | Open |
| Kingdom of Rhodoks | Meme formable; Italian-based kingdom from Mount & Blade: Warband | Open |
| Rhineland | | Open |
| Ostrogothic Kingdom | | Open |
| Visigothic Kingdom | | Open |
| Kingdom of the Vandals | | Open |
| Ryukyu Pirates | See notes below | Open |
| Kaido Bakufu ("Shogunate of the Seas") | See notes below | Open |
| Bronze Age nations | | Open |
| Samo's Empire | | Open |
| Illyria | Formable for Bosnia and Croatia when they hold all of Bosnia, Croatia and Slavonia (not Slovenia). Flag without the tricolor. | Open |
| Brandenburg | Make it a formable for nations with Brandenburgish culture | Open |

**Ryukyu Pirates (the more historical one):** imagine the young Ryukyu Kingdom falling to pirates before it becomes a Ming tributary. In game, the three Ryukyu provinces usually unify early into the vanilla Ryukyu Kingdom formable, and you can't take them over or spawn there as pirates. The idea is to remove the ruling family and either set up a new, piracy-focused Ryukyu Kingdom or turn it into a Pirate Republic.

**Kaido Bakufu (less historical, but fits a large pirate nation better):** Kaido means "road" or "sea route" and was often used for maritime trade lines. Bakufu was the name for the Tokugawa government after Japan was unified. Together that is roughly "Maritime Shogunate": a pirate republic that exploits the Sengoku conflict, defeats some of the splintered clans and proclaims its own shogunate. "Shogunate of the Seas" works if English names are preferred.

### Content

**Characters**
- Otto von Bismarck for the German Empire
- Caesar for Rome
- Hammurabi for Babylon

**HRE emperor chain (big request; might be a submod):** the HRE character starts as "King of the Romans" until Protestantism spawns. An event chain then leads to him being proclaimed emperor, based on his skill, the actions taken during his reign and his relationship with the Pope.

**Alternate flags**
- Coptic Egypt and Catholic Tunis: they still show the crescent
- Cordoba (Abd al-Rahman III flag)
- Celtic Union (2 options)
- Alpland

**Units**
- Winged hussars and late winged hussars for the Jagiellonian Empire, if possible

> The reference images for the flag requests were Discord CDN links. Discord links expire, so they almost certainly no longer load. Re-download them from the original Discord posts if you still have access. The original links are listed under "Archived reference links" at the end of this file.

### Mechanics
- [ ] Mod-based formables category. For example, Divergence of Darkness would have the Danubian Federation, Elbia, Dual Monarchy and so on.
- [ ] Colour picker for nations, with 1 to 3 alternatives each.

---

## 4. Tooling

### 4.1 Existing: `find_empty_triggers.py`

**Purpose:** finds, and can remove, empty trigger blocks. These cause this EU5 error:

```
[jomini_trigger.cpp:1111]: Invalid size of trigger container input evaluation weights
```

**What it detects**
- `potential = { }`
- `allow = { }`
- `trigger = { }`
- `AND = { }`, `OR = { }`, `NOT = { }`
- `limit = { }`
- `visible = { }`, `enabled = { }`, `available = { }`
- Blocks that contain only whitespace or comments

**Scope:** scans every `.txt` and `.gui` file. It skips `readme.txt` and `readme.md`, plus the `.git`, `__pycache__` and `node_modules` folders.

**Requirements:** Python 3.6 or newer, no dependencies. Runs on Windows, macOS and Linux.

**Usage**
```bash
# Scan only (default). You can also drag the mod's root folder onto the script.
python find_empty_triggers.py "C:\path\to\mod"

# Auto-fix, with a preview and a yes/no confirmation
python find_empty_triggers.py "C:\path\to\mod" --fix     # or -f
```

**Scan mode**
- Prints each issue with its line number and surrounding context.
- Within each file, issues are listed bottom-to-top. Working down the list therefore fixes the file from the bottom up, so the line numbers you haven't reached yet stay correct.

**Fix mode**
- Shows which files will change and how many issues each has.
- Asks for confirmation (`yes` or `y`).
- Writes a `.backup` copy next to every file before changing it.
- To undo a fix, copy the backup back:
  - Windows: `copy "my_file.txt.backup" "my_file.txt"`
  - Linux/Mac: `cp my_file.txt.backup my_file.txt`

**When to run it**
- When you see the trigger container error
- After adding reforms, decisions or events
- Before publishing an update
- After merging code from other sources

**Common causes of empty blocks:** copy-paste errors, unfinished implementations, removed commented-out code, template mistakes and merge conflicts.

**Cautions**
- Line numbers drift after manual edits, so rely on the context lines.
- Some empty blocks were deliberate placeholders.
- Test the mod after every auto-fix, and delete the `.backup` files once you're happy.

**Troubleshooting**
- **Window closes immediately:** the current version pauses with "Press Enter to exit". Otherwise, run it from a terminal.
- **Unicode errors:** the output is ASCII only (`[OK]`, `[WARNING]`, `[!]`), so this shouldn't happen.
- **Fix mode does nothing:** make sure you typed `yes` or `y`, check that the files are writable, and read the console output.

### 4.2 Planned: Formables list checker
- [ ] Make a text file listing every formable in the mod, sorted by rank.
- [ ] Make a tool that compares the `formable_countries` folder against that list and reports new or missing formables, so the list is easy to keep up to date.

### 4.3 Planned: Update Manager
- [ ] Written in C#. `run.bat` runs it and `build.bat` builds it.
- [ ] Integrate the existing variable updater.
- [ ] "Check outdated files" feature that lists outdated files in a built-in mod file browser.
- [ ] Visual side-by-side comparison of base game files and mod files.
- [ ] Settings button for changing the mod and base game directories.
- [ ] Automatic detection of the game directory.

> 4.2 could be a feature of the Update Manager rather than a separate tool, since both compare mod files against a reference.

---

## 5. Parked code: Bactrian Synod restoration events

These events let the Bactrian Synod restore Macedonia (`BACTR.5`), Assyria (`BACTR.6`) and Persia (`BACTR.7`) as Greco-Buddhist vassal kingdoms. They are parked until they're updated.

All three use the same pattern:

1. Pick a random owned location in the target lands.
2. Create a new country there at kingdom rank.
3. Form the formable on it and set its map colour.
4. Create a Greco-Buddhist ruler and set the country's and the ruler family's religion.
5. Make it a vassal of the event's country.
6. Hand over every owned location in the target lands, cored and fully integrated.

| Event | Target lands | Formable | Ruler culture |
|---|---|---|---|
| BACTR.5 | Areas: macedonia, albania, northern_greece, thrace | `BMCDN_f` | greek |
| BACTR.6 | Area: jazira | `ASYRI_f` | syriac |
| BACTR.7 | Region: persia | `BPSNE_f` | farsi |

> Each event repeats the same ~45 lines. When they're updated, one scripted effect with `$LIMIT$`, `$FORMABLE$`, `$COLOR$` and `$CULTURE$` parameters could replace most of that.

```
# Bactrian Synod event for restoring Macedonia
flavor_BACTR.5 = {
	type = country_event
	title = flavor_BACTR.5.title
	desc = flavor_BACTR.5.desc
	fire_only_once = yes
	option = {
		name = flavor_BACTR.5.a
		custom_tooltip = { text = BACTR_event_trigger_1_tt }
		hidden_effect = {
			random_owned_location = {
				limit = {
					OR = {
						area = area:macedonia_area
						area = area:albania_area
						area = area:northern_greece_area
						area = area:thrace_area
					}
				}
				save_scope_as = target_location
			}
			scope:target_location = {
				create_country_from_location = {
					save_scope_as = macedonia_nation
					set_country_rank = country_rank:rank_kingdom
				}
			}
			scope:macedonia_nation = {
				form_country = formable_country:BMCDN_f
				change_country_color = map_BMCDN
				create_character = {
					save_scope_as = macedonia_ruler
					culture = culture:greek_culture
					religion = religion:fnr_greco_buddhism_religion
				}
				set_new_ruler = scope:macedonia_ruler
				change_religion = religion:fnr_greco_buddhism_religion
				change_religion_for_ruler_and_family = {
					country = scope:macedonia_nation
					religion = religion:fnr_greco_buddhism_religion
				}
				make_subject_of = {
					target = root
					type = subject_type:vassal
				}
			}
			every_owned_location = {
				limit = {
					OR = {
						area = area:macedonia_area
						area = area:albania_area
						area = area:northern_greece_area
						area = area:thrace_area
					}
				}
				change_location_owner = scope:macedonia_nation
				add_core = scope:macedonia_nation
				change_integration_level = core
			}
		}
	}
}

# Bactrian Synod event for restoring Assyria
flavor_BACTR.6 = {
	type = country_event
	title = flavor_BACTR.6.title
	desc = flavor_BACTR.6.desc
	fire_only_once = yes
	option = {
		name = flavor_BACTR.6.a
		custom_tooltip = { text = BACTR_event_trigger_2_tt }
		hidden_effect = {
			random_owned_location = {
				limit = {
					area = area:jazira_area
				}
				save_scope_as = target_location
			}
			scope:target_location = {
				create_country_from_location = {
					save_scope_as = assyria_nation
					set_country_rank = country_rank:rank_kingdom
				}
			}
			scope:assyria_nation = {
				form_country = formable_country:ASYRI_f
				change_country_color = map_ASYRI
				create_character = {
					save_scope_as = assyria_ruler
					culture = culture:syriac_culture
					religion = religion:fnr_greco_buddhism_religion
				}
				set_new_ruler = scope:assyria_ruler
				change_religion = religion:fnr_greco_buddhism_religion
				change_religion_for_ruler_and_family = {
					country = scope:assyria_nation
					religion = religion:fnr_greco_buddhism_religion
				}
				make_subject_of = {
					target = root
					type = subject_type:vassal
				}
			}
			every_owned_location = {
				limit = {
					area = area:jazira_area
				}
				change_location_owner = scope:assyria_nation
				add_core = scope:assyria_nation
				change_integration_level = core
			}
		}
	}
}

# Bactrian Synod event for restoring Persia
flavor_BACTR.7 = {
	type = country_event
	title = flavor_BACTR.7.title
	desc = flavor_BACTR.7.desc
	fire_only_once = yes
	option = {
		name = flavor_BACTR.7.a
		custom_tooltip = { text = BACTR_event_trigger_3_tt }
		hidden_effect = {
			random_owned_location = {
				limit = {
					region = region:persia_region
				}
				save_scope_as = target_location
			}
			scope:target_location = {
				create_country_from_location = {
					save_scope_as = persia_nation
					set_country_rank = country_rank:rank_kingdom
				}
			}
			scope:persia_nation = {
				form_country = formable_country:BPSNE_f
				change_country_color = map_BPSNE
				create_character = {
					save_scope_as = persia_ruler
					culture = culture:farsi_culture
					religion = religion:fnr_greco_buddhism_religion
				}
				set_new_ruler = scope:persia_ruler
				change_religion = religion:fnr_greco_buddhism_religion
				change_religion_for_ruler_and_family = {
					country = scope:persia_nation
					religion = religion:fnr_greco_buddhism_religion
				}
				make_subject_of = {
					target = root
					type = subject_type:vassal
				}
			}
			every_owned_location = {
				limit = {
					region = region:persia_region
				}
				change_location_owner = scope:persia_nation
				add_core = scope:persia_nation
				change_integration_level = core
			}
		}
	}
}
```

---

## Archived reference links (Discord, probably expired)

- Baden-Wurttemberg flag: https://media.discordapp.net/attachments/1435551326753787974/1444360299174952970/2560px-Flag_of_Baden-WC3BCrttemberg_28state2C_lesser_arms29.png
- Cordoba alternate flag: https://media.discordapp.net/attachments/1435551326753787974/1441081302169288734/Flag_of_Abd_al-Rahman_III_of_Cordoba.jpg
- Celtic Union alternate flag 1: https://media.discordapp.net/attachments/1435551326753787974/1438321124042739896/celticflag.png
- Celtic Union alternate flag 2: https://media.discordapp.net/attachments/1435551326753787974/1438320777941487728/tumblr_ph5sonxndN1tl6bfv_1280.png
- Illyria flag: https://media.discordapp.net/attachments/1435551326753787974/1439607625967734926/a-flag-of-illyria-i-made-recently-v0-b3jag42iyqje1.png
- Alpland alternate flag: https://media.discordapp.net/attachments/1435551326753787974/1438322306316505261/alpine_empire_by_dementorflagchamber_dd47qfs-fullview.png
