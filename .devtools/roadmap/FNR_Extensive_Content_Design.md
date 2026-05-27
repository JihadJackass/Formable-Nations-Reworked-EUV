# FNR Content Roadmap -- Extensive Content Design Document

This document details specific, implementable content ideas for each update pack. Content types referenced throughout: Advances, Events (standalone + chains), International Organizations (IOs), Modifiers (country + province), Units, Building Types, Government Reforms, Decisions, Estate Privileges, Heir Selection, Societal Value interactions, Court/Liturgical Languages, Custom Cultures/Religions, and Cosmetic Tags.

---
---

## 1. PAX ROMANA

### Advances

**Renovatio Imperii Tree (ERE/Roman Empire path):**
- "Legacy of Justinian" -- unlocks Reconquest CB against former Roman territories; +10% manpower in owned Roman core provinces
- "Codex Civilis" -- stability boost, reduced unrest from wrong-culture pops, enables Roman legal system modifier
- "Themata Administration" -- unlocks Theme system building, +15% tax in provinces with Theme buildings
- "Greek Fire Refinement" -- unlocks Greek Fire naval modifier, +20% naval combat advantage in home waters
- "Autocrator's Authority" -- removes penalty for revoking noble privileges, +1 diplomatic reputation
- "Pentarchy Restored" -- available after controlling all 5 Pentarchy seats; massive religious unity bonus, unlocks Ecumenical Council decision

**Pax Romana Tree (WRE/Latin path):**
- "Foederati Integration" -- allows barbarian culture acceptance at reduced cost; mixed-culture military bonus
- "Renovatio Occidentalis" -- legitimacy bonus for controlling Rome + Ravenna + Milan; unlocks Western Imperial Court modifier
- "Limes Reconstruction" -- unlocks Limes building chain, fortification bonus along historical frontier provinces
- "Senatorial Revival" -- republic/monarchy hybrid option; Senate estate gains unique privileges
- "Latin Universalis" -- court language spread bonus; Latin-speaking pops give +research

**Gallic Revival Tree (Gallic Empire):**
- "Vercingetorix's Legacy" -- morale bonus when fighting in Gallic territory, culture conversion speed for Gallo-Roman
- "Druidic Restoration" -- religious conversion events for Gallo-Roman religion, unlocks sacred grove building
- "Gaulish Metallurgy" -- production bonus for iron/weapons goods in Gallic provinces
- "Arverni Confederation" -- unlocks tribal confederation IO mechanic for Gallic subjects

### Event Chains

**"The Last Triumph" (Roman Empire restoration chain, 8-12 events):**
1. "Echoes of the Forum" -- upon forming Rome, flavor about the weight of history; choose between Republican nostalgia or Imperial ambition (sets variable for later events)
2. "The Senate Convenes" -- if Republican path: establish a Senate estate with unique mechanics. If Imperial: gain autocratic bonuses but risk civil war
3. "Barbarian Ambassadors" -- neighboring non-Roman nations react to your claim; diplomatic events with acceptance/hostility outcomes
4. "The Hippodrome Roars" -- chariot faction events (Blues vs Greens); each faction provides different bonuses but choosing one risks revolt from the other
5. "Plague of Justinian's Shadow" -- random plague event; decisions about quarantine (lose trade income, save pops) vs. open borders (keep income, lose pops)
6. "The Walls Hold" -- defensive event when a major power declares war; Theodosian Wall modifier for Constantinople
7. "Triumph Through the Golden Gate" -- after winning a major war, triumphal procession event with prestige and legitimacy
8. "Roma Aeterna" -- final capstone event after holding all core Roman territory for 25+ years; permanent "Eternal Rome" modifier

**"The Fourth Crusade Reversed" (Latin Empire chain, 5 events):**
1. "Baldwin's Throne" -- upon forming Latin Empire, choose how to handle Orthodox population (tolerance vs. forced conversion)
2. "The Partition of Romania" -- distribute territory to Crusader vassals or centralize; affects stability vs. vassal loyalty
3. "Venetian Demands" -- Venice demands trade concessions; refuse (war risk) or accept (economic penalty)
4. "Greek Resistance" -- Nicaean/Epirote pretenders emerge; military challenge events
5. "The Latin Rite Takes Root" -- after 50+ years, religious blending event; option to create a unique Uniate rite

**"The Ptolemaic Renaissance" (Ptolemaic Kingdom chain, 6 events):**
1. "The Library Reborn" -- establish the Great Library; choose focus (military science, philosophy, medicine) for different advance bonuses
2. "Cleopatra's Shadow" -- dynastic intrigue events; female ruler bonus path
3. "The Nile's Bounty" -- agricultural events tied to flood mechanics; good floods = surplus events, bad floods = famine
4. "Greek and Egyptian" -- cultural synthesis events; option to create a hybrid Greco-Egyptian culture
5. "Pharaoh or Basileus?" -- choose Egyptian or Greek court traditions for different government reform paths
6. "Mare Nostrum" -- naval expansion events for controlling eastern Mediterranean trade

**"The Gothic Kingdom" (Gothia chain, 4 events):**
1. "Crimean Refuge" -- establishing the last Gothic outpost; survival against steppe nomads
2. "The Bible of Wulfila" -- Arian Christianity events; religious identity vs. assimilation
3. "Genoese Neighbors" -- relations with Italian trading colonies in Crimea
4. "Gothic Renaissance" -- if Gothia reaches kingdom rank, cultural revival event with unique Gothic culture bonuses

**"Magna Graecia Reborn" (Magna Graecia chain, 4 events):**
1. "The Italiote League" -- form a defensive league among Greek-speaking southern Italian cities
2. "Syracuse's Legacy" -- Archimedes-themed engineering events; siege defense bonuses
3. "The Griko Tongue" -- decisions about preserving Greek language vs. Latinization
4. "Tyrant or Democrat" -- government form events, choosing between Syracusan tyranny (military bonuses) or Athenian democracy (trade/research bonuses)

**"Pontic Revival" (Pontus chain, 3 events):**
1. "Mithridates' Heir" -- claim the legacy of Pontus; gain claims on Black Sea coast
2. "The Pontic Greeks" -- cultural preservation events in Anatolia
3. "Black Sea Dominion" -- trade control events for Black Sea commerce

### International Organizations

**Roman Senate IO:**
- Type: Internal political body
- Members: Roman Empire + any nation with Latin court language that accepts
- Mechanics: Voting on policy changes (war declarations require Senate approval or lose legitimacy; trade agreements get bonuses through Senate ratification)
- Policies: "Senatorial Oversight" (stability bonus, ruler power penalty), "Imperial Prerogative" (reverse), "Provincial Autonomy" (reduced unrest, reduced tax)

**Pentarchy IO:**
- Type: Religious authority
- Members: Nations controlling Rome, Constantinople, Alexandria, Antioch, Jerusalem
- Mechanics: Ecumenical councils that set Christian doctrine; majority votes determine religious bonuses for all Christian nations
- Policies: "Council Supremacy" vs. "Papal Primacy" vs. "Patriarchal Autocephaly"

**Foederati Pact IO:**
- Type: Military alliance for Roman vassal integration
- Members: Rome + barbarian subjects
- Mechanics: Barbarian subjects get military access and subsidies; in exchange Rome gets auxiliary troops. Subjects can eventually be integrated or revolt.

### Modifiers

**Country Modifiers:**
- "Renovatio Imperii" -- +15% prestige, +10% diplomatic reputation, +5% core creation cost reduction (applied on forming any Roman successor)
- "Roman Legal Tradition" -- -10% unrest, +10% governing capacity, +5% tax (from Codex Civilis advance)
- "Crisis of the Third Century" -- negative modifier applied during civil wars: -20% tax, -15% manpower, +25% rebel strength
- "Bread and Circuses" -- +10% stability, -5% tax income (decision-activated, costs gold monthly)
- "Praetorian Influence" -- +10% army morale, -15% legitimacy, +25% pretender rebel chance (from relying too heavily on guard units)
- "Gothic Isolation" -- +25% defensiveness, -15% trade income, +10% fort defense (Gothia-specific)
- "Hellenistic Synthesis" -- +10% research, +5% tolerance of heathens, +10% culture conversion (for Ptolemaic/Magna Graecia/Bactria)

**Province Modifiers:**
- "Roman Roads" -- +15% movement speed, +10% trade value, +5% tax (buildable in former Roman provinces)
- "Limes Fortification" -- +25% fort defense, +10% garrison size, -5% development cost (frontier provinces only)
- "Imperial Forum" -- +20% tax, +10% prestige from province, +5% pop growth (capital province only)
- "Hippodrome" -- +10% stability impact, +5% unrest (from faction riots), +15% prestige
- "Aqueduct System" -- +10% pop growth, +5% tax, -10% plague spread chance

### Units

- "Limitanei" -- cheap border garrison infantry; high defensiveness, low offense; available to all Roman formables
- "Comitatenses" -- elite mobile field army; balanced stats, bonus when reinforcing; mid-tier unlock
- "Cataphract" -- super-heavy cavalry; devastating charge, slow movement; ERE specialty
- "Varangian Guard" -- elite bodyguard infantry; very high morale and shock, small stack size; requires Norse/Scandinavian accepted culture
- "Excubitors" -- palace guard; high discipline, loyalty bonus reducing civil war chance
- "Greek Fire Ship" -- naval unit; bonus in narrow sea zones (Aegean, Bosporus), devastating against galleys
- "Bucellarii" -- private retinue cavalry; fast, good for raiding; available to Gothic/barbarian Roman paths

### Building Types

- "Theme Garrison" -- military/administrative hybrid; provides local defense troops + tax bonus; requires Themata Administration advance
- "Limes Watchtower" -- frontier fort chain; cheaper than full fort, provides vision and attrition to enemies; chain: Watchtower > Burgus > Castellum
- "Imperial Forum" -- capital-only building; massive prestige and stability bonus; expensive, long build time
- "Aqueduct" -- province building; pop growth and sanitation bonus; reduces plague impact
- "Sacred Grove" -- Gallic Empire exclusive; provides Gallo-Roman religion conversion and monthly piety; replaces church
- "Hippodrome" -- large city building; stability and prestige, but can trigger faction riot events
- "Great Library" -- Ptolemaic exclusive; massive research bonus, attracts scholars event chain

### Government Reforms

- "Tetrarchy" -- split realm administration; +governing capacity, but co-emperor events can cause instability; unlocks after controlling 300+ provinces
- "Dominate" -- absolute autocracy; +tax, +legitimacy, -noble estate influence, -stability from decentralization
- "Principate" -- balanced monarchy; moderate bonuses across the board; first among equals flavor
- "Gallic Confederation" -- tribal federation reform for Gallic Empire; subjects get autonomy but provide guaranteed levies
- "Basileus Autokrator" -- ERE exclusive; supreme religious and secular authority combined; +legitimacy, +religious unity, enables excommunication-like mechanic
- "Exarchate Administration" -- for controlling distant Roman territories; reduced governing penalty for far-flung provinces

### Decisions

- "Restore the Hippodrome" -- requires capital = Constantinople, 500 gold; adds Hippodrome building and triggers chariot faction events
- "Issue a New Legal Code" -- requires stability > 50, Codex Civilis advance; adds Roman Legal Tradition modifier for 50 years
- "Bread and Circuses" -- toggle decision; spend monthly gold for stability bonus
- "Proclaim the Renovatio Imperii" -- requires owning Rome + Constantinople + Alexandria; massive one-time prestige, triggers diplomatic events with all neighbors
- "Triumph of the Emperor" -- available after winning a major war; costs prestige to enact, gives legitimacy and military tradition

### Custom Content

- Culture: Gallo-Roman (already exists for Gallic Empire)
- Religion: Gallo-Roman religion (already exists)
- Language: Gaulish (already exists as court/liturgical)
- New culture potential: "Romano-Gothic" for Gothia if they hold Italian/Roman territory long enough
- New religion potential: "Imperial Cult Revival" for pagan Roman paths

---
---

## 2. KAISERSCHLACHT

### Advances

**Prussian Militarism Tree:**
- "Kadettenschule" -- military academy system; +10% army drill gain, +5% discipline
- "Krumper System" -- hidden reserve training; +15% manpower recovery, enables rapid mobilization decision
- "Auftragstaktik" -- mission-type tactics; +10% army morale, +5% movement speed; generals gain initiative
- "Needle Gun Doctrine" -- late-game infantry modernization; +15% infantry combat ability
- "Generalstab" -- General Staff institution; +1 free general, +10% army tradition retention

**Zollverein Economic Tree:**
- "Customs Union Foundation" -- enables Zollverein IO creation; +5% trade income for all members
- "Railway Mania" -- +20% movement speed in German provinces with railway building, +10% trade goods produced
- "Industriegrundszeit" -- industrial revolution events; +15% production in urban provinces, triggers urbanization events
- "Rhine Commerce" -- +10% trade income in Rhine-adjacent provinces; enables Rhine trade node bonuses
- "Made in Germany" -- +10% goods produced, +5% trade steering; late-game capstone

**Kleinstaaterei Mechanics Tree (for minor German states):**
- "Imperial Circles" -- organizing regional defense; +10% fort defense for circle members
- "Reichskammergericht" -- Imperial court system; -10% unrest, +5% stability; requires HRE membership
- "Landeshoheit" -- territorial sovereignty; +10% governing capacity, enables independence faction
- "Mediatization" -- annexing minor states legally; reduced AE for annexing German minors
- "German Confederation" -- post-Napoleonic reorganization; enables Confederation IO

### Event Chains

**"The Road to Ems" (German Unification chain, 10 events):**
1. "The German Question" -- initial event when forming NGF or SGF; Grossdeutsch vs. Kleindeutsch decision (include Austria or not)
2. "Schleswig-Holstein Crisis" -- diplomatic crisis with Denmark; war or negotiation paths
3. "The Punctation of Olmutz" -- humiliation event if Austria blocks unification; choose to accept (lose prestige) or resist
4. "Seven Weeks' War" -- if Kleindeutsch, war with Austria becomes inevitable; rapid victory events
5. "The Ems Dispatch" -- diplomatic provocation event; edited telegram triggers French response
6. "Sedan" -- decisive battle event; capture of enemy ruler; massive prestige
7. "The Hall of Mirrors" -- proclamation of Empire at Versailles; formation event with massive bonuses
8. "Kulturkampf" -- post-unification religious conflict; Catholic vs. Protestant estate tensions
9. "The Social Question" -- industrialization creates worker unrest; Bismarckian welfare state decisions
10. "Dropping the Pilot" -- ruler dismisses powerful chancellor; stability risk vs. autocratic freedom

**"The Rheinbund" (Rhine Confederation chain, 6 events):**
1. "Napoleon's Shadow" -- forming the Confederation under foreign patronage vs. genuine independence
2. "The Diet of the Confederation" -- establishing governance; centralized vs. federalist structure
3. "Mediatization Wave" -- absorbing minor counts and lords; gain provinces but anger nobles
4. "Continental System" -- trade embargo events; economic hardship vs. French alliance benefits
5. "The War of Liberation" -- when protector weakens, opportunity to break free or double down
6. "The Congress System" -- post-war reorganization; shape the new German order

**"The Sorbian Awakening" (Sorbic Kingdom chain, 5 events):**
1. "The Last Slavic Voice" -- cultural survival event; investing in language preservation
2. "Between Two Worlds" -- navigating German and Slavic identity; cultural decisions
3. "The Lusatian League" -- forming a Sorbian defensive confederation
4. "Pan-Slavic Brothers" -- diplomatic events with Poland/Bohemia; alliance opportunities
5. "Great Sorbia Proclaimed" -- expansion events when reaching Great Sorbia; reaction from German neighbors

**"Prussia's Transformation" (Ducal Prussia > Brandenburg-Prussia chain, 6 events):**
1. "The Secularization" -- Teutonic Order transforms into secular duchy; religious consequences
2. "The Hohenzollern Inheritance" -- dynastic union with Brandenburg; political maneuvering
3. "The Great Elector" -- military reform events; building the Prussian army from scratch
4. "Huguenot Refugees" -- immigration event; accept French Protestants for economic/military bonus
5. "The Soldier King" -- obsessive militarization; giant grenadier events, economic austerity
6. "Frederician Enlightenment" -- philosopher-king events; tolerance, legal reform, cultural patronage

**"Hanseatic Revival" (Hanseatic League chain, 5 events):**
1. "The Kontore" -- establishing trade offices in foreign cities
2. "Piracy on the Baltic" -- dealing with Vitalienbruder pirates
3. "The Hansetag" -- League assembly decisions; trade policy votes
4. "Dutch Competition" -- rivalry events with Netherlands over trade supremacy
5. "From Merchants to Princes" -- transforming trade wealth into political power

**"Elbian Federation" (Elbian Federation chain, 4 events):**
1. "The Elbe Unites" -- rivers as connectors rather than borders; trade route events
2. "Bohemian-Brandenburg Synthesis" -- Czech-German cultural fusion events
3. "The Amber Road" -- controlling the ancient trade route from Baltic to Mediterranean
4. "Federation or Empire?" -- choice between loose federation (more autonomy, trade) or centralized empire (more military, less stability)

### International Organizations

**Zollverein (Customs Union) IO:**
- Type: Economic union
- Leader: Largest German economy
- Mechanics: Shared trade bonuses, tariff policy votes, economic integration events
- Policies: "Free Trade" (+trade, -domestic production protection), "Protectionist" (reverse), "Industrial Policy" (+production, requires investment)
- Members gradually economically integrate; after 50 years, political union becomes possible

**German Confederation IO:**
- Type: Political federation
- Leader: Rotating presidency or strongest member
- Mechanics: Collective defense obligation, but internal rivalries; Austria vs. Prussia leadership struggle events
- Policies: "Bundesreform" (centralization attempts), "Status Quo" (maintain balance), "Trias" (third force of middle states)

**Imperial Circle IO:**
- Type: Regional defense pact within HRE
- Mechanics: Mutual defense within circle, shared military infrastructure
- Smaller scope than full HRE but more responsive

### Modifiers

**Country:**
- "Prussian Discipline" -- +15% discipline, +10% army tradition, -5% army maintenance; earned through Prussian militarism advances
- "Zollverein Prosperity" -- +10% trade income, +5% production efficiency; all Zollverein members
- "Kleinstaaterei Paralysis" -- -10% diplomatic reputation, -5% stability; applied to fragmented German nations pre-unification
- "Kulturkampf" -- -10% religious unity, +5% stability from secularization; post-unification event modifier
- "Realpolitik" -- +10% improve relations, -5% aggressive expansion impact; Bismarckian diplomacy
- "Blood and Iron" -- +10% army morale, +5% war exhaustion reduction; wartime modifier after speech event
- "Hanseatic Tradition" -- +15% trade income, +10% naval force limit, -5% land force limit
- "Sorbian Resilience" -- +10% defensiveness, +15% culture conversion resistance, +5% stability

**Province:**
- "Rhine River Trade" -- +15% trade value for Rhine-adjacent provinces
- "Ruhr Industrial Basin" -- +20% production, +10% urban pop growth; specific to Ruhr-area provinces
- "Prussian Fortification" -- +20% fort defense, +10% garrison; for Prussian fortress provinces
- "Hanseatic Kontor" -- +10% trade power, +5% trade steering; for cities with Hanseatic offices
- "University Town" -- +10% research, +5% institution spread; for provinces with universities (Gottingen, Heidelberg, etc.)

### Units

- "Prussian Grenadier" -- heavy shock infantry; high morale, bonus in offensive battles
- "Jager" -- light infantry skirmisher; bonus in forest/hill terrain, good reconnaissance
- "Landwehr" -- militia reserve; cheap, mediocre stats, but very fast to raise; Krumper System unlock
- "Uhlan" -- light lancer cavalry; fast movement, good for flanking and pursuit
- "Kurassier" -- heavy cavalry; devastating charge, slow; late-game unlock
- "Hanseatic Kogge Marines" -- naval infantry specializing in boarding actions
- "Freikorps" -- irregular volunteer unit; bonus in guerrilla warfare, can be raised without manpower

### Building Types

- "Kadettenschule" -- military academy; +army tradition, +drill gain; one per state
- "Zollhaus" -- customs house; +trade value, +tariff income; border provinces
- "Eisenbahn" -- railway; +movement speed, +trade goods transport, +pop migration; expensive, requires Industriegrundszeit
- "Bergwerk" -- expanded mine; +production of metals/minerals; specific to mining provinces
- "Garnisonskirche" -- garrison church; +army morale recovery, +religious unity in province; Prussian flavor
- "Rathaus" -- town hall; +governing capacity, +stability in province; available to all German formables
- "Festung" -- modernized fortress; +fort defense beyond normal forts; Prussian specialty

### Government Reforms

- "Prussian General Staff" -- +1 general, +10% army tradition, rulers must have military skill 3+ or face events
- "Bundesrat Federation" -- federal council governance; subjects have voting rights, +stability, harder to centralize
- "Enlightened Absolutism" -- Frederician reform; +research, +tolerance, ruler makes all decisions
- "Rhenish Confederation" (already exists as Rheinkonfoderation) -- expand with more mechanics
- "Mediatized Monarchy" -- for states that absorbed minor lords; +governing capacity, noble estate starts stronger
- "Merchant Republic of the Hanse" -- Hanseatic specific; trade-focused republic with elected Burgermeister

### Decisions

- "Convene the Zollverein" -- requires 3+ German nations willing; creates Customs Union IO
- "Proclaim Kleindeutschland" -- requires NGF + owning southern German provinces; excludes Austria, forms German Empire
- "Proclaim Grossdeutschland" -- requires owning Austrian core territory; includes Austria, different flag/modifier
- "Issue the Carlsbad Decrees" -- censorship decision; +stability, -research, -liberty desire of subjects
- "The Emancipation Edict" -- free serfs; short-term instability, long-term economic and manpower bonus
- "Establish the Reichstag" -- create parliamentary body; +stability, noble estate loses some power
- "Mobilize the Landwehr" -- emergency mobilization decision; raises Landwehr units rapidly but costs stability

---
---

## 3. DEUS VULT

### Advances

**Crusader Military Tree:**
- "Castle Architecture" -- unlocks Krak-style fortress building; +25% fort defense in Levant
- "Military Order Integration" -- military orders provide permanent garrison units; +10% discipline for order units
- "Crusader Charge" -- heavy cavalry shock bonus; +15% cavalry combat ability
- "Siege Warfare of the East" -- learned from Muslim opponents; +10% siege ability
- "Frontier Vigilance" -- border defense doctrine; +15% attrition for enemies in owned territory

**Outremer Governance Tree:**
- "Haute Cour" -- high court system; noble estate gains unique Crusader privileges but provides military bonuses
- "Assise de Jerusalem" -- legal code; -15% unrest, +10% stability; unique feudal law
- "Trading Privileges" -- Italian merchant concessions; +20% trade income, but Italian republics gain trade power too
- "Poulain Culture" -- local-born Crusader identity; +10% tolerance of other religions, new cultural events
- "Lingua Franca" -- multilingual administration; -5% culture conversion cost, +10% diplomatic reputation

### Event Chains

**"The Fall and Rise of Edessa" (County of Edessa chain, 5 events):**
1. "Baldwin's Gambit" -- establishing the first Crusader state; relations with Armenian Christians
2. "Joscelin's Dilemma" -- Armenian vs. Frankish noble factions; choose which to favor
3. "Zengi at the Gates" -- major siege event; desperate defense decisions
4. "The County Falls" -- if territory is lost, exile events with reconquest mission
5. "Edessa Restored" -- if reconquered, rebuilding events with new defensive focus

**"Antioch the Great" (Principality chain, 6 events):**
1. "Bohemond's Pride" -- conflict with Byzantium over suzerainty; accept Byzantine overlordship (safety) or refuse (independence but isolation)
2. "The Siege of Antioch" -- legendary siege events; discovering the Holy Lance
3. "Norman and Greek" -- cultural tension between Norman rulers and Greek population
4. "The Field of Blood" -- major defeat event; recovery and adaptation
5. "Reynald's Recklessness" -- rogue vassal events; vassal breaks truce, consequences for all
6. "Antioch Endures" -- if held for 100+ years, permanent establishment modifier

**"Kingdom of Heaven" (Outremer formation chain, 8 events):**
1. "The True Cross" -- relic events; carrying it into battle provides morale bonus but losing it is catastrophic
2. "Horns of Hattin" -- major battle decision; choose to fight or retreat; catastrophic if lost
3. "The Third Crusade Arrives" -- reinforcement event; European monarchs arrive with armies
4. "Richard and Saladin" -- diplomatic events; truce negotiations, mutual respect flavor
5. "Frederick's Crusade" -- diplomatic crusade; gaining territory through negotiation rather than conquest
6. "The Barons' Crusade" -- minor crusade reinforcement; new settlers and soldiers
7. "The Mamluk Threat" -- escalating danger from Egypt; prepare defenses or seek alliance
8. "Outremer Eternal" -- if held for 200+ years, the Crusader states become a permanent fixture; massive prestige, unique culture evolution

**"The Orders Militant" (Military Orders chain, 5 events, applies to any Crusader state):**
1. "Founding the Order" -- establish a military order; choose focus (hospital/military/banking)
2. "The Rule of the Order" -- internal governance; strict vs. relaxed discipline
3. "Templar Bankers" -- financial services events; massive income but political jealousy
4. "The Order's Ambition" -- order becomes too powerful; events where they challenge royal authority
5. "Trial of the Order" -- suppression or reform; disband for their wealth or reform into loyal servants

### International Organizations

**Crusader States Mutual Defense IO:**
- Type: Military alliance
- Members: All Crusader formables + Kingdom of Jerusalem
- Mechanics: Automatic call to arms against Muslim neighbors; shared military access; joint campaigns
- Policies: "Permanent Crusade" (always at war posture, military bonuses), "Pragmatic Peace" (trade with Muslims allowed, diplomatic bonuses), "Fortification Focus" (defensive bonuses, building cost reduction)
- Special: If one member falls, others get "Avenge the Fallen" CB and war subsidies

**Military Order IO:**
- Type: Transnational religious-military organization
- Members: The Order's commanderies across multiple nations
- Mechanics: Order provides garrison troops to any Christian nation that grants them land; in exchange they gain autonomy
- Can evolve into sovereign entity (like historical Teutonic/Hospitaller states)

### Modifiers

**Country:**
- "Crusader Zeal" -- +15% morale, +10% manpower, -5% diplomacy; active during crusade wars
- "Outremer Born" -- +5% discipline, +10% trade income, +5% tolerance; for Poulain-generation rulers
- "Defender of the Holy Land" -- +20% fort defense in Levant provinces, +10% prestige; requires controlling Jerusalem
- "Templar Treasure" -- +25% interest per annum, +10% gold income; but -10% papal relations
- "Military Order Garrison" -- +10% garrison size, +5% fort defense; provinces with Order commanderies
- "Crusader Isolation" -- -10% diplomatic reputation, -5% trade; if no European ally has access

**Province:**
- "Krak-style Fortress" -- +30% fort defense, +15% garrison; Crusader fortress building
- "Pilgrim Route" -- +15% trade value, +5% tax; provinces on pilgrimage paths
- "Commandery" -- +10% garrison, +5% religious unity; Military Order building
- "Crusader Settlement" -- +10% development cost reduction, +5% Frankish culture growth
- "Holy Site" -- +20% religious unity, +10% prestige from province; Jerusalem, Bethlehem, Nazareth, etc.

### Units

- "Crusader Knight" -- elite heavy cavalry; very high shock, high maintenance; the iconic Crusader unit
- "Turcopole" -- light cavalry recruited from local converts; fast, cheap, good reconnaissance
- "Sergeant-at-Arms" -- solid medium infantry; reliable backbone of Crusader armies
- "Military Order Knight" -- Templar/Hospitaller variant; higher discipline than regular knights, cannot retreat (fanatic)
- "Pilgrim Militia" -- cheap defensive infantry; raised from pilgrim populations, low quality but free
- "Maronite Archer" -- local Christian auxiliary; good ranged damage, knowledge of terrain

### Building Types

- "Krak des Chevaliers" -- mega-fortress; extremely expensive, +40% fort defense, +25% garrison; one per state
- "Commandery" -- Military Order base; provides Order troops, +religious unity, +garrison
- "Pilgrim Hospice" -- heals attrition, +pop growth from pilgrim settlement, +trade value
- "Crusader Cathedral" -- religious building; +religious unity, +prestige, +stability; higher tier than normal church
- "Sugar Plantation" -- economic building unique to Levant Crusader states; +trade goods, +production

### Government Reforms

- "Haute Cour Feudalism" -- Crusader high court; noble estate has more power but provides better military, unique succession (election among vassals)
- "Military Theocracy" -- for Military Order states; no dynasty, elected Grand Master, pure military focus
- "Merchant Crusader Republic" -- for Italian-influenced Crusader states; trade focus, elected doges
- "Poulain Administration" -- mixed governance; tolerance of local customs, reduced conversion but better stability

---
---

## 4. RULE BRITANNIA

### Advances

**Parliamentary Evolution Tree:**
- "Magna Carta Principles" -- -10% noble estate influence maximum, +5% stability from decentralization
- "Model Parliament" -- enables Parliamentary government reform; estate balance bonuses
- "Bill of Rights" -- +10% stability, -15% revolt risk, legitimacy floor of 40
- "Cabinet Government" -- +1 advisor slot, advisors cost -15%; ministerial government
- "Westminster System" -- exportable governance; subjects with this advance are more loyal

**Naval Supremacy Tree:**
- "Ship of the Line Doctrine" -- +10% heavy ship combat ability, +5% naval morale
- "Navigation Acts" -- +15% trade steering to home node, -10% foreign trade in home waters
- "Press Gang" -- +20% sailor recovery, -5% stability; wartime naval manning
- "Admiralty Board" -- +1 admiral, +10% naval tradition; professional naval command
- "Pax Britannica" -- +25% naval force limit, +10% trade income globally; late-game naval hegemony

**Colonial Administration Tree:**
- "Royal Charter" -- enables chartered company buildings; trade company provinces get +10% income
- "Colonial Office" -- -10% colonial maintenance, +5% colonial growth
- "Dominion Status" -- subjects gain autonomy but remain loyal; +10% subject liberty reduction
- "Imperial Preference" -- trade bonuses between mother country and colonies; tariff system

### Event Chains

**"The Angevin Inheritance" (Angevin Empire chain, 8 events):**
1. "Henry's Realm" -- controlling England and half of France; managing dual inheritance
2. "Thomas Becket's Shadow" -- church vs. crown conflict; murder or compromise
3. "Eleanor's Court" -- powerful queen events; cultural patronage or political scheming
4. "The Devil's Brood" -- succession crisis; sons rebel against father (historical Henry II parallel)
5. "Lionheart Abroad" -- ruler goes on crusade; regent events at home, glory abroad
6. "John's Folly" -- weak successor events; losing French territory or fighting to keep it
7. "The Provisions" -- baronial reform demands; accept (parliamentary path) or refuse (civil war)
8. "Dual Crown Consolidated" -- after 100 years, if held together, permanent Angevin modifier

**"Camelot's Return" (Camelot chain, 5 events):**
1. "The Sword in the Stone" -- legitimacy event; Arthurian prophecy fulfillment for Cornish ruler
2. "The Round Table" -- establish a chivalric council; unique estate mechanic with named knights
3. "The Quest for the Grail" -- religious/chivalric expedition events; success grants holy relic modifier
4. "Morgan's Treachery" -- court intrigue events; betrayal from within
5. "Avalon Found" -- if Camelot controls all of Britain, mystical event chain with permanent modifiers

**"The Great Scotia" (Great Scotia expansion, 4 events, building on existing):**
1. "The Declaration of Arbroath" -- independence declaration; diplomatic weight event
2. "The Auld Alliance" -- Franco-Scottish alliance events; call France to war vs. England
3. "Nova Scotia Founded" -- colonial events (already discovers Acadia); settler events in New World
4. "The Scottish Enlightenment" -- if stability > 70 and age 5+, massive research and culture events

**"Commonwealth of Nations" (British Empire chain, 6 events):**
1. "The Sun Never Sets" -- upon forming British Empire, global map event showing extent
2. "The Jewel in the Crown" -- India integration events; direct rule vs. company rule
3. "White Dominions" -- settler colony self-governance events; Canada/Australia/NZ autonomy
4. "The Great Game" -- Central Asian rivalry events (with Russia)
5. "Imperial Conference" -- dominions meet to discuss shared policy; IO mechanics
6. "Winds of Change" -- decolonization pressure events; choose graceful transition or resist

**"The Anglo-Dutch Enterprise" (Anglo-Dutch Union chain, 4 events):**
1. "William's Crossing" -- Glorious Revolution parallel; Dutch stadtholder takes English throne
2. "The Act of Union" -- formal merger of English and Dutch institutions
3. "Maritime Hegemony" -- combined naval power dominates global trade
4. "VOC and EIC United" -- merged trading companies create global commercial empire

**"The Celtic Dawn" (Celtic Union chain, 5 events):**
1. "The Bards Sing" -- cultural revival event; investment in Celtic languages and traditions
2. "Druidic Whispers" -- pre-Christian Celtic religious revival option
3. "The Gaelic League" -- pan-Celtic political movement; uniting Irish, Scottish, Welsh, Breton, Cornish
4. "Tara's Crown" -- establishing a high kingship; choosing seat of power
5. "The Green and Gold" -- if Celtic Union reaches empire rank, permanent cultural modifier

### International Organizations

**British Commonwealth IO:**
- Type: Imperial federation
- Members: British Empire + dominions/colonies
- Mechanics: Trade preference system, mutual defense, dominion autonomy levels
- Policies: "Imperial Federation" (centralized, military focus), "Free Association" (loose, trade focus), "Dominion Autonomy" (subjects self-govern but remain allied)

**Angevin Dual Court IO:**
- Type: Personal union governance
- Members: English and French crowns
- Mechanics: Managing two separate court systems; events about which court gets priority
- Policies: "English Primary" (favor English nobles, lose French loyalty), "French Primary" (reverse), "Itinerant Court" (balance, but expensive)

### Modifiers

**Country:**
- "Britannia Rules the Waves" -- +20% naval combat, +15% trade steering; requires 50+ heavy ships
- "The Wooden Wall" -- +25% naval defense, enemy cannot naval invade without 2:1 ratio
- "Splendid Isolation" -- +10% stability, -5% diplomatic reputation; no continental alliances
- "Imperial Overstretch" -- -10% stability, -5% tax; if controlling more than 1000 provinces without sufficient governing capacity
- "Arthurian Legend" -- +15% legitimacy, +10% prestige, +5% morale; Camelot-specific
- "Highland Fury" -- +15% shock damage, +10% movement in hills/mountains; Scottish units
- "Celtic Renaissance" -- +10% research, +10% culture conversion for Celtic cultures

### Units

- "Longbowman" -- elite ranged infantry; devastating at range, vulnerable in melee; English specialty
- "Redcoat" -- professional line infantry; high discipline, fire damage bonus; post-age 5
- "Highland Charge" -- Scottish shock infantry; devastating first attack, weaker in prolonged combat
- "Welsh Spearman" -- defensive infantry; anti-cavalry bonus, good in mountains
- "Royal Marine" -- amphibious infantry; bonus when attacking from ships, coastal warfare
- "Kern" -- Irish light infantry; fast, cheap, good for raiding; Celtic Union available
- "Gallowglass" -- heavy Norse-Gaelic mercenary infantry; very high combat ability, expensive

### Building Types

- "Royal Dockyard" -- +naval force limit, +ship repair speed, +trade; coastal provinces only
- "Parliament House" -- capital building; enables Parliamentary reform, +stability, +legitimacy
- "Celtic Hill Fort" -- fortification for Celtic nations; cheaper than standard forts, bonus in hilly terrain
- "Trading Company Office" -- colonial trade building; +trade income, +colonial growth; overseas only
- "Round Table Hall" -- Camelot exclusive; +prestige, +chivalric event chance, +legitimacy

### Government Reforms

- "Parliamentary Monarchy" -- ruler shares power with parliament; +stability, -ruler power, elected ministers
- "Cromwellian Commonwealth" -- Commonwealth of England; republic with military focus, religious overtones
- "Celtic High Kingship" -- Celtic Union; elected high king from constituent kingdoms, war council mechanic
- "Angevin Dual Monarchy" -- managing two kingdoms; special succession rules, court split mechanics
- "Scottish Enlightened Monarchy" -- Great Scotia; +research, +diplomatic reputation, university bonus

---
---

## 5. FROM VISTULA TO VOLGA

### Advances

**Pan-Slavic Unity Tree:**
- "Slavic Brotherhood" -- +10% relations with Slavic nations, +5% culture acceptance speed
- "The Glagolitic Tradition" -- literacy and cultural preservation; +5% research, unique religious flavor
- "Slavic Congress" -- enables Pan-Slavic IO; diplomatic weight for Slavic nations
- "Hussite Legacy" -- military and religious reform; +10% infantry combat, +5% religious tolerance
- "Cossack Frontier" -- steppe warfare traditions; +15% cavalry combat, +10% colonization speed

**Jagiellonian Dynasty Tree:**
- "Royal Marriage Network" -- +2 diplomatic reputation, personal union chance +25%
- "Privilege of Neminem Captivabimus" -- noble rights; +10% noble estate loyalty, -5% centralization
- "Nihil Novi" -- nothing new without noble consent; +stability from decentralization, -ruler power
- "The Lublin Example" -- real union mechanics; convert personal union to constitutional union
- "Jagiellonian Golden Age" -- if controlling POL+LIT+HUN+BOH, massive cultural/research bonuses

### Event Chains

**"The Moravian Experiment" (Great Moravia expansion, 6 events beyond existing):**
1. "Cyril and Methodius' Legacy" -- already touches on Orthodox Moravia; expand with theological debate events
2. "The Diet of Free Moravians" -- council governance events; voting on policy changes
3. "Between Rome and Constantinople" -- choosing religious alignment; each path gives different bonuses
4. "The Slavic Pope" -- if Moravian Orthodox spreads enough, propose a Slavic patriarchate
5. "Nitra's Children" -- dynasty events; meritocratic succession in action (already have heir selection)
6. "Moravian Renaissance" -- if stability > 80 and research high, cultural golden age event

**"The Jagiellonian Dream" (Jagiellonian Empire chain, 7 events):**
1. "Four Crowns" -- upon achieving union of Poland, Lithuania, Hungary, Bohemia
2. "The Diet's Objection" -- each kingdom's nobles resist centralization; individual estate events
3. "Jagiellonian Justice" -- legal harmonization across four kingdoms; choose unified or separate codes
4. "The Turkish Menace" -- shared defense against Ottoman expansion; military coordination events
5. "Reformation Pressures" -- different kingdoms lean different religious directions; manage or enforce unity
6. "The Vasa Complication" -- Swedish dynastic claims create fifth front; opportunity or crisis
7. "Empire Proclaimed" -- after 50 years of stable union, option to formalize as single empire

**"Zapadoslavia" (West Slavic Union chain, 5 events):**
1. "The Slavic Idea" -- Pan-West-Slavic nationalism awakening
2. "Prague or Warsaw" -- which city leads; choosing capital affects national character
3. "The German Neighbor" -- managing relations with Germanic powers; alliance or rivalry
4. "Slavic Industry" -- economic development events; Bohemian glass, Polish grain, Silesian coal
5. "A Third Way" -- positioning between East (Russia) and West (Germany); unique diplomatic path

**"The Yugoslav Vision" (Yugoslavia chain, 5 events):**
1. "South Slav Congress" -- initial unification proposals; idealistic vs. pragmatic approaches
2. "Serbian Leadership" -- Serbia's claim to lead vs. Croatian/Slovenian resistance
3. "The Vidovdan Constitution" -- centralist vs. federalist constitutional debate
4. "Tito's Brotherhood" -- if communist path, brotherhood and unity ideology events
5. "The Fracture Lines" -- ethnic tension events that can be managed or spiral; historical foreshadowing

**"Kyivan Rus Restored" (Kyivan Rus chain, 5 events):**
1. "Vladimir's Baptism Reversed" -- reclaiming the original Rus heritage
2. "The Veche Restored" -- popular assembly governance; democratic elements in medieval setting
3. "Rus vs. Muscovy" -- rivalry with Moscow over who is the true heir of Rus
4. "The Cossack Question" -- integrating Cossack frontier communities; military vs. autonomy balance
5. "Ruthenian Renaissance" -- cultural golden age; Ukrainian/Belarusian literary flowering

### International Organizations

**Pan-Slavic Congress IO:**
- Type: Cultural-political alliance
- Members: All Slavic nations
- Mechanics: Shared cultural defense, diplomatic coordination, mutual language bonuses
- Policies: "Pan-Slavic Solidarity" (mutual defense, cultural bonuses), "Slavic Commonwealth" (trade and research sharing), "National Sovereignty" (loose association, diplomatic reputation only)

**Jagiellonian Dynastic Union IO:**
- Type: Personal/constitutional union
- Members: Poland, Lithuania, Hungary, Bohemia (and subjects)
- Mechanics: Shared dynasty, coordinated foreign policy, but independent internal governance; voting on war declarations, trade policy
- Special: If one member's dynasty dies, succession crisis events for all

**Balkan League IO:**
- Type: Military alliance
- Members: South Slavic nations
- Mechanics: Anti-Ottoman coordination; shared intelligence, military planning, but also internal rivalries
- Policies: "War Council" (aggressive, anti-Ottoman focus), "Diplomatic Front" (European great power support seeking), "Internal Reconciliation" (address Serb-Croat-Bosniak tensions)

### Modifiers

**Country:**
- "Hussite War Wagon Tradition" -- +20% infantry combat, +15% defensiveness; if Hussite religion
- "Cossack Host" -- +15% cavalry combat, +10% manpower from steppe provinces; requires Cossack culture acceptance
- "Jagiellonian Legacy" -- +10% diplomatic reputation, +15% personal union maintenance; dynasty-specific
- "Yugoslav Brotherhood" -- +10% stability, -5% unrest for accepted cultures; multi-ethnic bonus
- "Wendish Crusade Survivor" -- +10% defensiveness, +5% fort defense; Wendish Empire specific
- "Moravian Meritocracy" -- +5% advisor cost reduction, +10% ruler skill chance; Great Moravia specific

### Units

- "Hussite War Wagon" -- mobile fortress unit; defensive infantry bonus, slow but devastating when dug in
- "Winged Hussar" -- iconic heavy cavalry; devastating charge, best cavalry in game; Polish/Jagiellonian unlock
- "Cossack Cavalry" -- fast light cavalry; excellent for flanking, raiding, and steppe warfare
- "Pandur" -- South Slavic irregular infantry; guerrilla specialist, terrain bonus in mountains/forests
- "Hajduk" -- Balkan rebel-turned-soldier; bonus in home territory, anti-Ottoman specialist
- "Zaporozhian Sich Warrior" -- elite Cossack infantry; high morale, amphibious (river warfare)

### Building Types

- "Veche Hall" -- governance building; +stability, enables popular assembly mechanics; Kyivan Rus specific
- "Tabor Fortification" -- Hussite mobile fort; provides defensive bonus even outside forts; Great Moravia
- "Cossack Sich" -- military settlement; provides cavalry units, frontier defense, colonization bonus
- "Slavic Academy" -- research building; +research, +cultural conversion resistance; Pan-Slavic nations
- "Boyar Estate" -- noble estate building; +tax from nobility, +local manpower; Eastern Slavic nations

---
---

## 6. CRESCENT AND STAR

### Advances

**Caliphate Administration Tree:**
- "Diwan System" -- bureaucratic governance; +15% governing capacity, +10% tax efficiency
- "Waqf Endowments" -- religious charitable foundations; +10% stability, +5% missionary strength
- "Jizya Administration" -- dhimmi taxation system; +10% tax from wrong-religion provinces, +5% tolerance of heathens
- "Barid Postal System" -- intelligence and communication network; +10% spy network, +5% diplomatic distance reduction
- "Commander of the Faithful" -- caliph title; +20% religious unity, +10% prestige, claim leadership of Muslim world

**Islamic Golden Age Tree:**
- "House of Wisdom" -- research institution; +15% research, +10% institution spread
- "Algebra and Algorithms" -- mathematical advances; +10% production efficiency, +5% trade efficiency
- "Islamic Medicine" -- medical advances; +10% pop growth, -15% plague impact
- "Astronomical Observatories" -- navigation and timekeeping; +10% naval range, +5% colonization
- "Arabic Calligraphy" -- cultural prestige; +10% prestige, +5% diplomatic reputation

**Assassin Shadow Tree (Hashashin-specific):**
- "The Old Man of the Mountain" -- ruler gains +20% spy network, +10% assassination chance against rival rulers
- "Fedayeen Training" -- elite assassin units; +25% shock for Fida'i units, can target enemy generals
- "Castle of Alamut" -- mountain fortress network; +30% fort defense in mountain provinces
- "The Invisible Hand" -- espionage network; can destabilize neighbors through events without declaring war
- "Paradise Garden" -- recruitment through indoctrination; +20% manpower, unique culture conversion

### Event Chains

**"The Caliphate Restored" (Caliphate formation chain, 7 events, shared across Umayyad/Rashidun/Abbasid/Fatimid):**
1. "Claiming the Mantle" -- declaring the caliphate; choose Sunni (Umayyad/Abbasid) or Shia (Fatimid) legitimacy
2. "The Ulema's Verdict" -- religious scholars accept or challenge your claim; depends on piety and control of holy cities
3. "Rival Claimants" -- other Muslim nations react; some accept, some declare rival caliphate
4. "The Hajj Revenue" -- controlling Mecca/Medina; massive income and prestige from pilgrimage
5. "Baghdad or Damascus" -- choosing capital affects national character; Baghdad = scholarship, Damascus = military, Cairo = trade
6. "The Translation Movement" -- Golden Age of translation; Greek/Persian/Indian knowledge absorbed
7. "Caliph of Islam" -- after 50+ years, if controlling majority of Muslim world, supreme religious authority modifier

**"Rise of the Assassins" (Hashashin chain, 6 events):**
1. "Hasan-i Sabbah's Vision" -- founding the Order; choosing between pure idealism and pragmatic power
2. "The Eagle's Nest" -- establishing Alamut as an impregnable fortress
3. "The Dagger and the Word" -- assassination vs. propaganda; each event lets you target a specific enemy leader or spread ideology
4. "Mongol Storm" -- existential threat event; prepare for Mongol invasion or flee
5. "The Shadow State" -- if surviving, build a hidden state within other nations; unique vassal-like mechanic
6. "The Assassin's Creed" -- capstone event; codifying the Order's principles for permanent bonuses

**"Neo-Babylonian Revival" (Babylon chain, 5 events):**
1. "The Ishtar Gate Rebuilt" -- reconstructing ancient Babylonian architecture; prestige event
2. "Hammurabi's Code Revisited" -- legal reform events; establishing ancient-styled law code
3. "The Hanging Gardens" -- building wonder event; massive prestige and development bonus
4. "Chaldean Astronomy" -- reviving Babylonian scholarship; research bonuses
5. "Nebuchadnezzar's Dream" -- imperial ambition event; claims on Levant and Egypt

**"The Sassanid Phoenix" (Sassanid chain, 6 events):**
1. "Fire of Ahura Mazda" -- Zoroastrian revival; religious conversion events
2. "Shahanshah of Iran" -- claiming the King of Kings title; massive legitimacy and prestige
3. "The Immortals Reborn" -- recreating the elite guard unit
4. "Ctesiphon Restored" -- rebuilding the ancient capital; massive building event
5. "The Silk Road Emperor" -- controlling east-west trade routes; economic events
6. "Revenge of the Sassanids" -- if defeating a major Arab/Turkish power, reversal-of-history events

**"Omani Maritime Empire" (Omani Empire chain, 5 events):**
1. "The Ibadi Way" -- unique Islamic sect identity; tolerant but distinct
2. "Zanzibar Connection" -- East African colonial expansion; establishing the clove trade
3. "The Imam's Fleet" -- naval power in the Indian Ocean
4. "Muscat vs. Zanzibar" -- empire splitting event; choose which half to focus on
5. "The Maritime Silk Road" -- connecting Arabian, Indian, and African trade networks

### International Organizations

**Caliphate Religious Authority IO:**
- Type: Religious leadership
- Leader: The Caliph
- Members: All Muslim nations that accept the Caliph's authority
- Mechanics: Religious rulings affect all members; Caliph can declare jihad (crusade equivalent), issue fatwas affecting member policies
- Policies: "Strict Sharia" (+religious unity, -tolerance), "Ijtihad" (interpretation allowed, +research, -unity), "Millet System" (+tolerance, -conversion)

**Assassin Shadow Network IO:**
- Type: Secret organization
- Leader: Grand Master (Old Man of the Mountain)
- Members: Hidden cells in various nations
- Mechanics: Can target any ruler for assassination attempts; diplomatic immunity through fear; nations pay protection money or face consequences
- Invisible to non-members; revealed only through spy networks

### Modifiers

**Country:**
- "Golden Age of Islam" -- +15% research, +10% production, +5% trade; triggered by House of Wisdom advance + stability > 60
- "Commander of the Faithful" -- +20% religious unity, +10% prestige, +5% army morale; Caliph title holder
- "Assassin's Reputation" -- +25% spy defense, enemies have -15% spy network construction; Hashashin-specific
- "Zoroastrian Revival" -- +10% fire damage (thematic), +10% legitimacy, +5% tolerance of heathens; Sassanid-specific
- "Babylonian Wonder" -- +20% prestige, +10% development cost reduction; after building Hanging Gardens
- "Ibadi Tolerance" -- +15% tolerance of heretics, +10% trade income; Omani-specific

**Province:**
- "House of Wisdom" -- +25% research, +10% institution spread; capital province, Abbasid-specific
- "Caravanserai" -- +10% trade value, +5% movement speed; trade route provinces
- "Madrasa" -- +10% religious unity, +5% research; province building
- "Ribat Fortress" -- +15% fort defense, +5% religious unity; frontier fortress
- "Bazaar" -- +15% trade goods produced, +5% urban pop growth; major city provinces
- "Sacred Mosque" -- +20% religious unity, +10% prestige from province; Mecca, Medina, Jerusalem, Damascus, Baghdad

### Units

- "Ghulam" -- slave-soldier heavy infantry; very high discipline, loyal (no revolt risk)
- "Mamluk Cavalry" -- elite slave-soldier heavy cavalry; highest-tier cavalry for Islamic nations
- "Fida'i" -- Assassin special unit; can be sent on assassination missions against enemy generals/rulers
- "Immortals" -- Sassanid elite guard; extremely high morale and discipline, small numbers
- "Janissary" -- (vanilla overlap, but unique Caliphate variant); convert captured soldiers into elite infantry
- "Bedouin Raider" -- light cavalry; excellent in desert terrain, good for scouting and raiding
- "Corsair" -- naval raider unit; bonus in coastal raids, can capture trade ships
- "Ayyar" -- urban militia/vigilante unit; bonus in siege defense, cheap to raise in cities

### Building Types

- "Madrasa" -- religious school; +religious unity, +research; higher tier than standard religious building
- "Caravanserai" -- trade building; +trade value, +movement speed; on trade routes
- "Ribat" -- frontier fortress-monastery; +fort defense, +religious unity, +garrison
- "Bimaristan" -- hospital; +pop growth, -plague impact; Islamic medical tradition
- "Hammam" -- bathhouse; +urban pop growth, +stability; city building
- "Dar al-Hikmah" -- House of Wisdom equivalent; mega-research building; capital only, Abbasid/Caliphate specific
- "Castle of Alamut" -- Hashashin mega-fortress; extreme fort defense in mountains, trains Fida'i units

### Government Reforms

- "Rashidun Shura" -- consultative caliphate; +stability, religious scholars advise, elected successor
- "Umayyad Hereditary Caliphate" -- dynastic; +legitimacy, +dynasty prestige, centralized
- "Abbasid Bureaucratic Caliphate" -- administrative; +governing capacity, +tax, vizier system
- "Fatimid Esoteric Caliphate" -- Ismaili mystical authority; +spy network, +religious influence abroad
- "Assassin Grand Master" -- theocratic-military hybrid; no dynasty, elected master, assassination as statecraft
- "Sassanid Shahanshah" -- King of Kings; Zoroastrian divine authority, satrapy system for provinces

### Custom Content

- Existing: Akkadian language/culture for Assyrian Empire
- New potential: "Neo-Babylonian" culture for Babylon
- New religion: "Revived Zoroastrianism" with specific mechanics for Sassanid (fire temple buildings, purity laws)
- Court language: Arabic, Persian, Akkadian variants for different caliphates

---
---

## 7. RISING SUN

### Advances

**Bushido Refinement Tree:**
- "Way of the Warrior" -- +10% army morale, +5% discipline; samurai ethos
- "Katana Mastery" -- +10% shock damage for Japanese infantry; melee superiority
- "Castle Town Development" -- +10% development in castle provinces, +5% fort defense
- "Seppuku Honor" -- generals never surrender; +15% morale but captured generals die
- "Sakoku Doctrine" -- isolation policy; +15% stability, +10% spy defense, -20% trade income from foreign merchants

**Mandate of Heaven Tree (China):**
- "Celestial Bureaucracy" -- +20% governing capacity, +10% tax; mandarin administration
- "Imperial Examinations" -- advisor cost -20%, +10% research; meritocratic system
- "Tributary System" -- enables Tributary IO; subjects pay tribute for protection/trade
- "Great Wall Maintenance" -- +25% fort defense on northern border, +10% attrition for northern invaders
- "Zheng He's Legacy" -- +20% naval range, +10% trade income from maritime routes; treasure fleet tradition

**Meiji Modernization Tree (Japan modern path):**
- "Opening the Country" -- ending isolation; +20% trade income, +15% institution spread, -10% stability initially
- "Conscription Army" -- +25% manpower, +10% discipline; replacing samurai with modern army
- "Zaibatsu" -- industrial conglomerate building; +20% production, +10% trade
- "Imperial Constitution" -- +10% stability, +5% legitimacy; constitutional monarchy
- "Fukoku Kyohei" -- "rich nation, strong army"; +10% tax, +10% army quality; national slogan

### Event Chains

**"The Warring States" (Japan unification chain, 8 events):**
1. "Three Unifiers" -- ruler archetype choice: Oda (ruthless efficiency), Toyotomi (diplomatic cunning), Tokugawa (patient strategy); each gives different modifiers
2. "The Burning of Mount Hiei" -- decision to destroy powerful temple; +military power, -religious unity
3. "Nanban Trade" -- Portuguese arrive with firearms; adopt or resist
4. "The Christian Question" -- growing Christian population; tolerate, regulate, or persecute
5. "Sword Hunt" -- disarm the peasantry; +stability, -revolt risk, but lose militia manpower
6. "Sankin-Kotai" -- alternate attendance; daimyo must maintain Edo residences, weakening them financially
7. "The Closed Country" -- Sakoku decision; massive isolation event with cascading effects
8. "The Black Ships" -- forced opening event; Perry-equivalent arrives, crisis of national identity

**"The Taiping Kingdom" (Taiping expansion chain, 5 events beyond existing):**
1. "Hong Xiuquan's Vision" -- already has religion creation; expand with specific prophetic events
2. "The Heavenly Capital" -- establishing Nanjing as capital; massive battle events
3. "Land Reform" -- radical redistribution; +stability in converted provinces, -tax initially
4. "The Ever-Victorious Army" -- foreign mercenary events; Western military advisors
5. "The Final Examination" -- climactic battle for control of China; succeed or fall

**"The Three Kingdoms of Korea" (Korean formables chain, 6 events):**
1. "Goguryeo's Pride" -- martial tradition; choosing aggressive vs. defensive posture
2. "The Imjin War" -- Japanese invasion defense events; turtle ship debut
3. "Admiral Yi's Genius" -- naval hero events; undefeatable at sea
4. "Hangul Revolution" -- King Sejong's alphabet; literacy boom, +research, +stability
5. "Hermit Kingdom" -- isolation policy; Korean Sakoku equivalent
6. "The Morning Calm" -- after unification, peaceful prosperity events

**"Empire of the Rising Sun" (Empire of Japan chain, 5 events):**
1. "Greater East Asia" -- IO already exists; expand with specific policy events
2. "Manchukuo" -- puppet state creation in Manchuria
3. "The Decisive Battle Doctrine" -- naval strategy events; all-or-nothing battle planning
4. "Industrial Mobilization" -- total war economy events
5. "The Divine Wind" -- desperate measures events; kamikaze tactics option in losing wars

### International Organizations

**Greater East Asia Co-Prosperity Sphere (already exists, expand with):**
- More detailed policies: "Japan First" (exploitative), "Co-Prosperity" (genuine mutual benefit), "Cultural Unity" (Japanization)
- Member events: puppet state loyalty events, resistance movements, economic integration
- Rivalry events with Western colonial powers

**Chinese Tributary System IO:**
- Type: Hierarchical alliance
- Leader: Emperor of China
- Members: Korea, Vietnam, various Southeast Asian states
- Mechanics: Tributes pay gold/goods for Chinese protection; China cannot refuse defensive call
- Policies: "Benevolent Overlord" (+trade, +stability for tributaries), "Strict Hierarchy" (+tribute income, -tributary loyalty), "Cultural Exchange" (mutual research bonus)

**Confucian Academy IO:**
- Type: Cultural/intellectual organization
- Members: Confucian nations
- Mechanics: Shared research bonuses, diplomatic reputation, harmonious relations between members

### Modifiers

**Country:**
- "Bushido Spirit" -- +15% army morale, +10% discipline, -5% manpower recovery; quality over quantity
- "Mandate of Heaven" -- +20% legitimacy, +15% stability; held by China's ruler, can be lost
- "Sakoku Isolation" -- +20% stability, +15% spy defense, -25% trade income, -10% tech speed
- "Heavenly Kingdom" -- +10% manpower, +15% religious unity (for Taiping religion), -10% diplomacy
- "Admiral Yi's Legacy" -- +20% naval combat in home waters; permanent Korean naval modifier
- "Manchurian Frontier" -- +15% cavalry combat, +10% manpower; Manchuria-specific

### Units

- "Samurai" -- elite heavy infantry; very high morale and discipline, expensive
- "Ashigaru" -- conscript infantry; cheap, decent stats when led by good general
- "Sohei" -- warrior monk; high morale, religious fanaticism bonus
- "Turtle Ship" -- armored warship; devastating in coastal waters, slow on open ocean
- "Hwarang" -- Korean elite warrior; high morale, balanced stats
- "Banner Cavalry" -- Manchu/Chinese elite cavalry; organized by banner system, very disciplined
- "Wokou" -- pirate/raider naval unit; bonus in coastal raiding, cheap
- "Teppo Ashigaru" -- firearm infantry; high fire damage, adoption of Western weapons

### Building Types

- "Castle Town (Jokamachi)" -- combined military/economic building; +fort defense, +trade, +pop growth
- "Zen Temple" -- +stability, +army discipline; spiritual training for warriors
- "Terakoya" -- local school; +research, +pop literacy; Tokugawa-era education
- "Zaibatsu Complex" -- industrial building; +production, +trade; modern Japan only
- "Forbidden City" -- Chinese palace mega-building; +legitimacy, +prestige, +governing capacity; capital only
- "Examination Hall" -- Chinese meritocracy building; +advisor quality, +research
- "Hwacha Battery" -- Korean rocket launcher emplacement; +fort defense, fire damage bonus in defense

---
---

## 8. SILK ROAD

### Advances

**Silk Road Commerce Tree:**
- "Caravanserai Network" -- +15% trade value on Silk Road provinces, +10% movement speed
- "Bactrian Banking" -- financial services; +10% interest income, +5% trade steering
- "Lapis Lazuli Monopoly" -- luxury goods control; +20% trade goods value for lapis/gems
- "Nomad-Merchant Synthesis" -- combining steppe mobility with merchant wealth; +10% trade, +10% cavalry combat
- "Crossroads of Civilizations" -- cultural exchange; +10% research, +5% tolerance of heathens

**Steppe Warfare Tree:**
- "Composite Bow Mastery" -- +15% cavalry combat, +10% shock; horse archer superiority
- "Feigned Retreat" -- tactical doctrine; +10% army morale, flanking bonus
- "Mongol Postal System (Yam)" -- intelligence and communication; +15% movement speed, +10% spy network
- "Siege of the Steppe" -- nomads learn siege warfare; +10% siege ability for horde nations
- "The Khan's Law (Yasa)" -- strict legal code; +15% discipline, -10% unrest; Horde-specific

### Event Chains

**"The Greco-Bactrian Dream" (Bactria expansion chain, 6 events beyond existing):**
1. "Alexander's Heirs" -- already sets Greek language; expand with choice between Greek and local identity
2. "The Indo-Greek Synthesis" -- Buddhist-Greek fusion events; philosophical debates
3. "Menander's Questions" -- ruler converts to Buddhism option; unique Buddhist-Greek culture path
4. "The Kushan Successor" -- expanding from Bactria into India; Gandhara art events
5. "Silk and Silver" -- controlling the western terminus of the Silk Road
6. "The Last Greek King" -- survival events; maintaining identity against Parthian/Kushan pressure

**"The Last Horde" (The Horde chain, 6 events):**
1. "Kill the Khans" -- the unique requirement (destroy all other hordes) triggers a celebration
2. "The Eternal Blue Sky" -- Tengri religious capstone; heaven's mandate for the steppe
3. "Pax Mongolica" -- peace and trade across the steppe; economic golden age
4. "The Yasa Codified" -- legal code for the unified steppe; governance mechanics
5. "The Great Hunt" -- annual hunt events; military exercise with bonuses
6. "The Kurultai" -- grand council; all steppe peoples assemble to confirm the Khan

**"Mountain Kingdom" (Pamiristan/Badakhshan chain, 4 events):**
1. "Roof of the World" -- establishing sovereignty in the highest mountains
2. "Ruby Mines of Badakhshan" -- legendary gem mines; trade good events
3. "The Wakhan Corridor" -- controlling the narrow pass; strategic chokepoint events
4. "Ismaili Traditions" -- unique Shia Ismaili religious events; Aga Khan parallel

**"The Hephthalite Revival" (Hephthalite chain, 5 events):**
1. "The White Huns Return" -- reclaiming the Hephthalite legacy
2. "Between Persia and China" -- diplomatic positioning between major powers
3. "The Gandhara Campaign" -- expanding into rich Buddhist heartland
4. "Nomad Settlers" -- transitioning from nomadic to settled civilization
5. "The Hephthalite Renaissance" -- if surviving 100+ years, cultural flowering

### International Organizations

**Silk Road Trade League IO:**
- Type: Trade alliance
- Members: Nations controlling Silk Road provinces
- Mechanics: Shared trade bonuses, caravan protection, standardized weights and measures
- Policies: "Free Passage" (open borders for merchants, +trade), "Toll Collection" (controlled access, +tax), "Caravan Guard" (military protection of trade routes)

**Steppe Confederation IO:**
- Type: Tribal alliance
- Members: Horde/nomadic nations
- Mechanics: Shared grazing rights, military cooperation, kurultai voting on war/peace
- Policies: "Eternal War" (constant raiding of settled nations), "Pax Steppica" (trade with settled nations), "The Great Ride" (coordinated invasion of a major settled power)

### Modifiers

**Country:**
- "Silk Road Master" -- +20% trade income, +10% diplomatic reputation; controlling 10+ Silk Road provinces
- "Mountain Fortress Kingdom" -- +25% defensiveness, +15% fort defense, -10% offensive capability
- "The Khan's Authority" -- +15% cavalry combat, +10% manpower, +5% discipline; Horde-specific
- "Bactrian Synthesis" -- +10% research, +10% tolerance, +5% trade; Greek-Eastern fusion

**Province:**
- "Silk Road Station" -- +15% trade value, +10% movement speed; key trade provinces
- "Ruby Mine" -- +20% trade goods value; Badakhshan-specific
- "Mountain Pass" -- +30% fort defense, +20% attrition for attackers; strategic chokepoint
- "Lapis Lazuli Deposit" -- +15% trade goods value; specific provinces in Afghanistan/Badakhshan
- "Yurt Camp" -- +10% cavalry manpower, +5% movement speed; nomadic province

---
---

## 9. VIVE LA FRANCE

### Advances

**French Absolutism Tree:**
- "Lit de Justice" -- king overrides parliament; +10% ruler power, -5% estate influence
- "Intendant System" -- royal administrators; +15% governing capacity, +10% tax
- "Versailles Court" -- +20% prestige, +10% diplomatic reputation; requires palace building
- "Droit Divin" -- divine right of kings; +15% legitimacy, religious backing of monarchy
- "Code Napoleon" -- legal reform; -15% unrest, +10% stability, +5% administrative efficiency

**Occitan Cultural Tree:**
- "Troubadour Tradition" -- +10% prestige, +5% diplomatic reputation; cultural soft power
- "Langue d'Oc Revival" -- +10% culture conversion resistance for Occitan cultures, +5% stability
- "Cathar Memory" -- religious tolerance events; +10% tolerance of heretics
- "Mediterranean Commerce" -- +15% trade income in Mediterranean provinces
- "The Albigensian Legacy" -- military and cultural resistance tradition; +10% guerrilla warfare bonus

### Event Chains

**"The Sun King's Dream" (French Empire chain, 7 events):**
1. "L'Etat, c'est moi" -- absolutism declaration; ruler gains massive power but risks resistance
2. "The Fronde" -- noble revolt against centralization; suppress or compromise
3. "Versailles" -- palace construction event; massive prestige but enormous cost
4. "The Revocation" -- revoking religious tolerance; gain religious unity, lose Huguenot population (brain drain)
5. "Colonial Empire" -- establishing overseas empire; trade company events
6. "The Revolution" -- if absolutism goes too far, revolution event chain; can be prevented or managed
7. "Napoleon's Shadow" -- post-revolution, military genius ruler events; rapid conquest but overextension

**"Carolingian Restoration" (Carolingian Empire chain, 6 events):**
1. "Charlemagne's Crown" -- claiming the Carolingian legacy; requires Carolingian dynasty or Aachen control
2. "The Partition" -- Carolingian division tradition; events about keeping the empire together vs. splitting
3. "Alcuin's Academy" -- Carolingian renaissance; education and culture events
4. "The Missi Dominici" -- royal inspectors; +governing capacity, anti-corruption
5. "Rome and Aachen" -- papal relations; coronation events, church-state balance
6. "The Empire Endures" -- if held together for 50+ years, the division tradition is broken; permanent unity modifier

**"Occitan Freedom" (Occitania chain, 5 events):**
1. "The Langue d'Oc" -- language revival; cultural identity events
2. "The Cathar Revival" -- religious reformation events; alternative Christianity path
3. "Toulouse or Montpellier" -- capital choice; each gives different bonuses
4. "The Mediterranean Republic" -- trade-focused governance option
5. "Provencal Golden Age" -- art, poetry, and troubadour culture flowering

### International Organizations

**Carolingian Realm IO:**
- Expand the existing centers_of_realm reform into a full IO
- Members: Carolingian successor states
- Mechanics: Shared defense, Missi Dominici inspection system, cultural unity

**Francophone Cultural IO:**
- Type: Cultural alliance
- Members: French-speaking nations
- Mechanics: Shared cultural prestige, diplomatic language bonus (French as lingua franca), mutual research
- Historical parallel: La Francophonie

### Modifiers

**Country:**
- "Le Roi Soleil" -- +25% prestige, +15% diplomatic reputation; absolutism capstone
- "Revolutionary Spirit" -- +20% army morale, +15% manpower, -10% stability; revolution active
- "Carolingian Legacy" -- +10% legitimacy, +10% vassal opinion; Carolingian dynasty modifier
- "Occitan Identity" -- +10% cultural conversion resistance, +10% trade income; Occitania-specific
- "Arpitan Mountain Spirit" -- +10% defensiveness, +5% fort defense; Arpitania-specific

### Units

- "Gendarme" -- French heavy cavalry; devastating charge, high morale
- "Franc-Archer" -- early French militia archer; cheap, decent ranged combat
- "Old Guard" -- Napoleonic-era elite infantry; highest morale in game, expensive
- "Cathar Perfecti Guard" -- Occitania religious warrior; high morale, religious fanatic bonus
- "Gascon Musketeer" -- light infantry skirmisher; good at ranged combat, fast movement

---
---

## 10. DYNASTY OF EAGLES

### Advances

**Habsburg Marriage Diplomacy Tree:**
- "Tu Felix Austria Nube" -- +25% personal union chance, +10% diplomatic reputation
- "Imperial Election Machine" -- +20% chance of winning HRE elections, +influence with electors
- "Pragmatic Sanction" -- female succession allowed; unlocks powerful events if female ruler
- "Dual Crown Administration" -- managing multiple distinct kingdoms; +15% governing capacity
- "Imperial and Royal" -- K.u.K. dual administration; unique modifier for A-H

**Militargrenze Frontier Tree:**
- "Military Frontier" -- border military colonies; +15% fort defense, +10% manpower on frontier
- "Grenzer Recruitment" -- frontier soldiers; unlocks Grenzer unit, free border defense troops
- "Frontier Settlement" -- colonization of military border; +10% development, +5% pop growth
- "Cordon Sanitaire" -- disease and invasion barrier; -20% plague spread, +15% attrition for invaders

### Event Chains

**"The Compromise" (Austria-Hungary expansion chain, 7 events beyond existing):**
1. "The Hungarian Diet" -- already has Ausgleich event; expand with Hungarian noble demands
2. "The Czech Question" -- Bohemia demands equal status; trialism vs. dualism debate
3. "The Nationalities Problem" -- pan-Slavic, pan-German, Hungarian nationalist pressures
4. "The Bosnian Crisis" -- annexation of Bosnia; international diplomatic crisis
5. "The Imperial Army" -- K.u.K. military integration challenges; language of command debates
6. "Archduke's Reforms" -- reform-minded heir events; federal restructuring proposals
7. "The Empire Holds" -- if managing all crises, permanent stability bonus; otherwise dissolution events

**"The Austrian Inheritance" (Austrian Empire chain, 5 events):**
1. "Maria Theresa's Challenge" -- female succession crisis; war of succession
2. "The Theresian Reforms" -- modernization of army, bureaucracy, education
3. "Joseph's Radicalism" -- enlightened despot goes too far; noble resistance
4. "Metternich's System" -- conservative order; stability through repression
5. "The Spring of Nations" -- 1848 revolution parallel; survive or fall

### International Organizations

**Austrian Compromise IO:**
- Type: Constitutional union
- Members: Austria + Hungary (+ potentially Bohemia, Croatia)
- Mechanics: Shared foreign policy and military, separate internal governance; Ausgleich renewal events every 10 years
- Policies: "Centralist" (Austrian dominance), "Federalist" (all kingdoms equal), "Dualist" (Austria-Hungary balance)

### Modifiers and Units

- "K.u.K. Administration" -- +10% governing capacity, -5% unrest for accepted cultures; dual monarchy bonus
- "Habsburg Intermarriage" -- +15% PU chance, -5% ruler stats (inbreeding); dynasty modifier
- "Grenzer" -- frontier infantry; bonus in border provinces, free maintenance in military frontier zones
- "Imperial Cuirassier" -- heavy cavalry; high shock, expensive, prestige unit
- "Honved" -- Hungarian national guard; good morale, moderate stats; Hungarian-specific
- "Kaiserjager" -- mountain infantry; terrain bonus in Alps, excellent in defense

---
---

## 11-20: REMAINING PACKS (Condensed)

### 11. RECONQUISTA
- **Key Events:** Fall of Granada chain (choose mercy or expulsion), Iberian Union formation, Maritime Age kickoff (Henry the Navigator events), Inquisition establishment (religious unity vs. brain drain), Treaty of Tordesillas (dividing the world with another power)
- **Key Advances:** Reconquista momentum tree (bonuses that grow as you reclaim territory), Maritime exploration tree, Convivencia tolerance tree (alternative to Inquisition)
- **Key IO:** Iberian Wedding IO (dynastic union of Castile-Aragon equivalent), Tordesillas Treaty IO (dividing colonial claims)
- **Key Units:** Tercio (pike-and-shot formation, extremely high discipline), Jinete (light cavalry, Moorish-influenced), Almogavar (shock infantry, mountain specialist)
- **Key Buildings:** Alcazar (fortress-palace), Navigation School, Mission (colonial religious building)

### 12. VARANGIAN
- **Key Events:** Kalmar Union formation/dissolution chain, Swedish Deluge (Baltic war events), Viking Age legacy events (early game), Finnish Winter events (defensive war bonuses), Icelandic Althing (parliamentary tradition)
- **Key Advances:** Viking heritage tree (raiding, navigation, settlement), Baltic dominion tree (trade, naval), Arctic survival tree
- **Key IO:** Kalmar Union IO (three-kingdom union with break-up mechanics), Baltic Trade IO (Hanseatic rival)
- **Key Units:** Caroliner (Swedish line infantry, extremely disciplined), Viking Huscarl Legacy (elite heavy infantry), Finnish Ski Troops (winter warfare specialist), Varangian (elite Norse mercenary)
- **Key Modifiers:** "Swedish Discipline" (+15% discipline, +10% drill), "Viking Heritage" (+10% naval combat, +10% colonization speed), "Arctic Resilience" (+20% winter attrition reduction)

### 13. MANIFEST DESTINY
- **Key Events:** State formation chains (each state gets 2-3 flavor events about founding, industry, identity), Mexican Empire succession crisis, Gran Colombia fracture chain (Bolivar's dream vs. regional interests), Trail of Tears (forced relocation events), Gold Rush events (California, Alaska), Civil War parallel (north vs. south state tension)
- **Key Advances:** Frontier expansion tree, Bolivarian liberation tree, Indigenous resistance tree (for native paths)
- **Key IO:** Organization of American States IO, Confederate IO (if civil war path), Pan-American Trade IO
- **Key Units:** Minuteman (militia, fast to raise), Rough Rider (cavalry), Gaucho Lancer (South American), Conquistador legacy units
- **Key Modifiers:** "Manifest Destiny" (+15% colonization speed, +10% movement in uncolonized territory), "E Pluribus Unum" (+10% tolerance of all cultures when 5+ accepted)

### 14. MONSOON
- **Key Events:** Chola maritime expedition chain (conquering Sri Lanka, Srivijaya raids), Philippine revolution chain (Katipunan uprising), Burmese unification wars, Vietnamese resistance against China, Malay sultanate trade events
- **Key Advances:** Indian Ocean trade tree, Chola naval tree, Spice monopoly tree, Theravada Buddhist tree
- **Key IO:** Indian Ocean Trade League IO, ASEAN parallel IO, Chola Maritime Empire IO
- **Key Units:** War Elephant (devastating shock, expensive), Chola Marine (amphibious infantry), Kris Warrior (Southeast Asian shock infantry), Gurkha (Nepali elite infantry)
- **Key Buildings:** Hindu Temple Complex (massive prestige + stability), Spice Warehouse (+trade goods), Rice Paddy improvement (+pop growth)

### 15. MORNING CALM (merge candidate with Rising Sun)
- **Key Events:** Turtle Ship development chain, Hangul invention, Joseon civil service exams, Japanese invasion defense, Korean partition
- **Key Units:** Turtle Ship (armored warship), Hwarang elite, Korean hwacha rocket artillery
- **Key Modifiers:** "Hermit Kingdom" (+15% defensiveness, +10% spy defense, -15% trade), "Joseon Scholarship" (+15% research, +10% stability)

### 16. MOTHERLAND
- **Key Events:** Time of Troubles chain (dynasty extinction, pretender wars, Polish intervention), Romanov ascension, Peter the Great modernization (Western vs. traditional debate), Emancipation of serfs, Bolshevik revolution (Soviet path only)
- **Key Advances:** Russian autocracy tree, Siberian expansion tree, Westernization debate tree
- **Key IO:** Soviet Bloc IO (satellite state management), Russian mir commune IO (agricultural reform)
- **Key Units:** Streltsy (musketeer guard, can revolt), Cossack Irregular (fast cavalry, frontier warfare), Imperial Guard (elite infantry post-modernization)
- **Key Modifiers:** "Russian Winter" (+30% winter attrition for enemies, -10% own winter attrition), "Third Rome" (+15% religious unity, +10% legitimacy, +5% prestige)

### 17. SHIELD OF CHRISTENDOM
- **Key Events:** Armenian merchant diaspora chain (trade network events spanning Europe to India), Georgian golden age events, Circassian resistance chain (mountain warfare against great powers), Armenian cultural preservation events
- **Key Advances:** Mountain fortress tree, Merchant diaspora tree, Caucasian unity tree
- **Key Units:** Armenian Fedayi (guerrilla infantry), Georgian Cavalry (heavy cavalry, high morale), Circassian Mountaineer (terrain specialist)
- **Key Modifiers:** "Caucasian Shield" (+20% fort defense in mountains, +10% attrition for attackers), "Armenian Merchant Network" (+15% trade income globally from diaspora)

### 18. HEART OF AFRICA
- **Key Events:** Battle of Adwa chain (defeating European colonizer, massive prestige), Solomonic dynasty events, Ethiopian Orthodox church events, Trans-Saharan trade events, Scramble for Africa resistance chain, Beta Israel Exodus events
- **Key Advances:** Ethiopian highland defense tree, Trans-Saharan commerce tree, Solomonic legitimacy tree
- **Key Units:** Ethiopian Shotel Warrior (curved sword infantry), Oromo Cavalry, Malagasy Pirogue Marine
- **Key Modifiers:** "Lion of Judah" (+15% legitimacy, +10% army morale; Ethiopian specific), "Highland Fortress" (+25% defensiveness in highland provinces)

### 19. PACIFIC HORIZON
- **Key Events:** Polynesian navigation chain (discovering new islands, establishing trade routes), Hawaiian unification under Kamehameha parallel, Cook contact events, Australian gold rush, Maori Wars chain
- **Key Advances:** Polynesian wayfinding tree (navigation, colonization), Colonial settlement tree
- **Key Units:** War Canoe (naval transport + combat), Maori Warrior (high morale shock infantry), Polynesian Navigator (exploration specialist)
- **Key Modifiers:** "Master Navigators" (+25% naval range, +15% colonization speed; Polynesian specific), "Island Chain" (+15% naval defense in home waters)

### 20. CROWNED REPUBLIC
- **Key Events:** Italian Wars chain (foreign invasion of Italy), Risorgimento unification chain, Machiavelli's Prince (political philosophy events), Venice vs. Genoa rivalry, Lombard League revival, Papal States conflict
- **Key Advances:** Italian Renaissance tree (art, science, architecture bonuses), Republican governance tree, Maritime trade tree
- **Key IO:** Italian Trade League IO (city-state trade alliance), Papal League IO (Catholic defense)
- **Key Units:** Condottiero (professional mercenary captain), Venetian Marine (amphibious infantry), Genoese Crossbowman (elite ranged infantry), Stradioti (Albanian/Greek light cavalry in Italian service)
- **Key Buildings:** Palazzo (prestige + governing), Arsenal (naval production, Venice-specific), Fondaco (trade warehouse for foreign merchants)
- **Key Modifiers:** "Renaissance Splendor" (+20% prestige, +15% research, +10% development cost reduction), "Merchant Prince" (+15% trade income, +10% diplomatic reputation)

---
---

## CROSS-PACK CONTENT OPPORTUNITIES

Several systems could span multiple packs and create interconnected content:

**Universal Heritage System:** Any nation that controls historically significant cities gets "Heritage" modifiers that stack -- owning Rome + Constantinople + Alexandria = "Heir of the Ancient World" super-modifier. This creates cross-pack incentives.

**Rival Caliphate/Papacy System:** Crescent and Star + Pax Romana create rival religious authority IOs that interact -- Caliphate vs. Pentarchy vs. Papacy, each competing for religious influence over neutral Christian/Muslim nations.

**Trade Route System:** Silk Road + Monsoon + Deus Vult all touch the same trade routes. A unified Silk Road/Indian Ocean/Mediterranean trade system where controlling nodes from different packs gives compound bonuses.

**Imperial Legitimacy System:** Multiple packs feature empire-tier formables that claim universal authority (Roman Empire, Carolingian, Caliphate, Chinese Mandate, British Empire). A "Universal Empire" interaction system where only one can truly hold the title at a time, with diplomatic consequences.

**Cultural Synthesis Events:** When formables from different cultural spheres control each other's territory for long enough, fusion events trigger -- Greco-Bactrian, Gallo-Roman, Poulain, Taiping Christianity, etc. This already exists for some (Gallic Empire, Bactria) but could be systematized.
