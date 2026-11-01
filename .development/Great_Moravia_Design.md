# Great Moravia - Design Spec

Status as of 3.1.0:
- **Shipped:** 1 advance, the Moravian Meritocratic Succession law, the Moravian Patriarchate IO, a few modifiers, the grouped Hungary/Slovakia/Moravia reforms, and unique events.
- **Not yet built:** the Great Moravia reforms.

Flavor text below has been spell-checked; otherwise it is as written. Effect lists are unchanged.

## Contents
1. Laws
2. Estate privileges
3. Government reforms
4. Units
5. Advances
6. Buildings
7. Events
8. Implementation notes

---

## 1. Laws

### Legal Code - Sudnyj Ludem
*Written by Cyril and Methodius, it consisted of 32 chapters. While it is obsolete by today's standards, we can modify and expand it, making it a law system for commoners that replaces local customary rules. Our nobles will be granted judicial power, but alongside them royal legal overseers will act as co-judges.*

| Effect | Value |
|---|---|
| Legislative efficiency | +10% |
| Tax efficiency | +5% |
| Communalism | +0.025 |
| Centralization | +0.025 |

### Succession Law - Moravian Meritocratic Succession *(shipped in 3.1.0)*
*After the death of Svatopluk I, the greatest ruler of Great Moravia, legend says his three sons divided the realm, which led to its demise. We must learn from that mistake. Both men and women may become ruler. They will be trained and educated in Nitra by the very best scholars, and may the best of them rule. But the family must hold together, for in that lies its power, so the gifted of our family shall serve in the administration.*

**Effects**
- Children are eligible
- The current ruler is excluded
- Male and female rulers are allowed
- Women are allowed in cabinet positions
- Female generals are allowed
- Female admirals are allowed
- Score per ability: +2.50
- Each family member in the cabinet or another position of power gives +5% crown power

### Military Law - Army Doctrine: Professional Army (Age of Reformation)
*Our armies might not be the biggest, and we might not have the best fighters, cavalry or cannons. But thanks to our high standards, every army we field has a better baseline than its rivals.*

| Effect | Value |
|---|---|
| Army morale | +0.10 |
| Manpower | +10% |
| Discipline | +5% |
| Quality | +0.10 |

### Liturgical Language / Orthodox Law - Church Slavonic
*The Solun Brothers, Cyril and Methodius, brought the light of Christianity to the Moravian lands, and with it a new language, Old Church Slavonic, which they created for the people of Moravia so that the Bible and the rites would be in a language the new believers understood. It was taught not only to the clergy but also became the language of administration. Now we are bringing it back.*

| Effect | Value |
|---|---|
| Max literacy | +5% |
| Cabinet efficiency | +5% |
| Spirituality | +0.10 |

---

## 2. Estate privileges

### Nobles - Druzhina
*In older times, men of privilege and princes kept a small personal retinue called the druzhina: an elite force trained and paid by the man they served. We can revive this tradition by letting nobles keep a limited number of warriors at their own expense, who must be sent to war when the crown commands. The Arab scholar Ibrahim ibn Yaqub, travelling across Europe in the 10th century, recorded that the druzhina of the Duke of Poland numbered as many as 3,000 men.*

| Effect | Value |
|---|---|
| Infantry power | +10% |
| Discipline | +2.5% |
| Unlocks | Druzhina unit (see Units) |
| Decentralization | +0.10 |

### Burghers - Royal Mint (Banske Mesta / Mining Towns)
*We grant the right to mint the state's coin to certain cities near the gold and silver mines that our north has in plenty. These towns carry the prefix Banske, from bana, meaning mine. This secures the authenticity of our coinage and reduces counterfeiting.*

| Effect | Value |
|---|---|
| Gold production | +5% |
| Silver production | +5% |
| Minting | +0.05 |
| Capital economy | +0.025 |
| Decentralization | +0.025 |

### Burghers - Royal Free Cities
*To weaken the nobles, we will give exclusive privileges to key cities and their residents, letting them run their own economy and administration in return for a larger tax base. This keeps the nobles from controlling our important centers of production, raises the cities' productivity and keeps our coffers full. "Free" because they are in the hands of their residents; "Royal" because they are owned directly by the crown.*

| Effect | Value |
|---|---|
| Building slots in towns and cities | +20 |
| Production efficiency | +5% |
| Burgher maximum tax | +5% |
| Development growth in urban locations | +0.0010 |
| Burgher food consumption | +20% |
| Capital economy | +0.025 |
| Plutocracy | +0.025 |

### Burghers - Winemakers of Balaton
*The wine of Balaton is among the most prestigious in Europe. Only the wines of Burgundy, Italy and distant Georgia can match it.*

| Effect | Value |
|---|---|
| Wine production | +15% |
| Market attraction | +5% |
| Prosperity growth | +0.10% |
| Capital economy | +0.05 |

### Peasants - Laborer Protection (Age of Absolutism)
*Just like the peasants, laborers have become a core part of the state economy. It would be wise to offer them some protection to keep them content.*

| Effect | Value |
|---|---|
| Production efficiency | +10% |
| Pop promotion | +10% |
| Pop growth | +0.02% |
| Estate satisfaction | +20% |
| Estate power | +33% |
| Free subjects | +0.10 |

### Peasants - Shepherds and Farmers Culture
*Our land has always been mostly rural, and that shows in our people. Most live in tightly knit villages and communities where everybody knows everybody. The most common professions are farmer and shepherd: farming families on the fertile flatlands and shepherd communities in the mountains and valleys. It would be foolish to change these deep-rooted ways of life.*

| Effect | Value |
|---|---|
| Wheat output | +10% |
| Livestock output | +10% |
| Wool output | +10% |
| Pop migration | -10% |
| Serfdom | +0.025 |
| Communalism | +0.05 |

---

## 3. Government reforms *(not yet built)*

| Reform | Type | Age |
|---|---|---|
| Heirs of Nitra | Minor | Tradition |
| Palatine (Palantir) | Minor | Tradition |
| Council of Free Moravians | Major | Renaissance |
| Moravian Unitary Federation | Major | Absolutism |

### Heirs of Nitra (Minor, Age of Tradition)
*It was tradition to send the eldest sons, the heirs, to Nitra, the old seat of power of the Duchy of Nitra, to learn to rule by governing its territory (Slovakia). We are reviving this tradition in the hope of raising wise rulers for the prosperity of the realm.*

| Effect | Value |
|---|---|
| Ability growth from child education | +30% |
| Proximity speed | -5% |
| Decentralization | +0.10 |

### Palatine (Palantir) (Minor, Age of Tradition)
*The palatine held the highest administrative and partly noble title. His main duties were economic: he managed the royal court and could represent the monarch in his absence. It was a position of great prestige, signalling both deep trust and high competence.*

| Effect | Value |
|---|---|
| Tax efficiency | +5% |
| Crown power | +5% |
| Expected court cost | -10% |
| Decentralization | +0.05 |

### Council of Free Moravians (Major, Age of Renaissance)
*The King held council with his counts. The kniezata formed the upper nobility, and the druzinici (voji) the lower nobility. In this council the King was "first count among counts". He delegated the governing of the land to the upper nobles, and of the cities and hradiska to the lower nobles. They received administrative and judicial power over their territories and paid tribute and tax to the King.*

| Effect | Value |
|---|---|
| Crown power | +10% |
| Cabinet efficiency | +10% |
| Control | +5% |
| Noble satisfaction | +20% |
| Government reform slots | +1 |
| Centralization | +0.10 |

### Moravian Unitary Federation (Major, Age of Absolutism)
*Today our lands are home to many peoples: Bohemians, Moravians, Slovaks, Germans and more. For the realm to work, we must respect these cultures to some degree. We will create provinces based on the peoples who live there. Each will elect its own local governors and send two representatives to serve in our parliament and cabinet. We understand that peasants may lack the necessary knowledge, so we will make school mandatory for children and fund university stipends for the best of them. In this way we hope the realm will stay in harmony and prosper.*

| Effect | Value |
|---|---|
| Peasants allowed in parliament | yes |
| Cabinet efficiency | +15% |
| Cultural capacity | +2.00 |
| Cabinet seats | +2 |
| Government reform slots | +1 |
| Humanist | +0.10 |
| Liberalism | +0.10 |

---

## 4. Units

### Druzhina (infantry; unlocked by the Druzhina privilege)

| Stat | Value |
|---|---|
| Maximum strength | 500 |
| Combat power | 1.50 |
| Frontage | 1.00 |
| Combat speed | 2.00 |
| Initiative | 1.00 |
| Flanking ability | 100% |
| Secure flank | 100% |
| Morale damage taken | -10% |
| Strength damage taken | (none) |
| Morale damage done | +5% |
| Strength damage done | +5% |

---

## 5. Advances

| Advance | Age | Effects |
|---|---|---|
| Crossroads of Europe | Traditions | +10% institution spread, +2.5% trade efficiency |
| Slavic Zeal | Traditions | +0.15 army morale |
| Winemakers of Balaton | Renaissance | +10% wine production, +0.02 prestige |
| Hradiska | Renaissance | Unlocks the Hradisko building |

**Crossroads of Europe:** *For centuries our lands have stood at the crossroads of German, Frankish, Byzantine, Latin and many other cultures, and at the crossroads of trade across Europe.*

**Slavic Zeal:** *According to our legends, our men, even in defeat, slaughtered Roman armies many times their size and struck fear into the greatest conquerors. Our spirit is unbreakable, and so are our armies.*

**Winemakers of Balaton:** *The wine of Balaton is one of the greatest in all of Europe. Only the wines of France, Italy and distant Georgia can compete with it.*

**Hradiska:** *In Great Moravia, the economic centers of the realm were the hradiska: fortified settlements close to a lord's estate or castle. We will bring back these rural centers to boost our production.*

> The Winemakers of Balaton name is used twice: once for an advance and once for a burgher privilege. They need different internal keys, or one of them needs a new name.

---

## 6. Buildings

### Hradisko (rural government building; unlocked by the Hradiska advance)

| Property | Value |
|---|---|
| Base price | 100 gold |
| Requirements | Rural location, not desert |
| Build time | 365 days |
| Max level | 1 |
| Construction demand | Masonry 4.0, Lumber 3.0, Tools 1.5 |
| Employment | 500 peasants, 100 laborers, 100 soldiers |
| Upkeep | Tools 0.4, Weapons 0.2 |
| Effects | +10% RGO output, +5 manpower, +5% control, can recruit soldiers |

---

## 7. Events

### Event 1 - Tomb of Svatopluk I
*My lord, we have most likely found the tomb of Svatopluk I, the great ruler of Great Moravia at its peak. Exploration is under way, and we have recovered a crown and a sword. They shall once again become symbols of the royal family's power and legitimacy.*

| Artwork | Created | Art quality | Bonus |
|---|---|---|---|
| Crown of Svatopluk | 9th century | 62 | +0.05 legitimacy |
| Sword of Svatopluk | 9th century | 62 | +0.05 army morale |

### Event 2 - Canonization of New Saints and Icons (Orthodox only)
*Today we have raised two people to sainthood. The first is Prince Rastislav, who asked for Christianity to be brought to the lands of Great Moravia. The second is Svatopluk I, who brought Great Moravia to its greatest extent and spread Christianity to new lands. With this we also commission three new icons: one of Rastislav, one of Svatopluk and one of Cyril and Methodius. Through them we reconnect with the roots of our Orthodoxy and make that bond stronger than ever. Amen.*

| Artwork | Created | Art quality | Bonus |
|---|---|---|---|
| Icon of Rastislav | When the event fires | 62 | +0.05% pop growth, +0.0010 monthly development |
| Icon of Svatopluk | When the event fires | 62 | +5% army morale recovery, +0.10 army morale |
| Icon of Cyril and Methodius | When the event fires | 70 | -10% pop conversion speed, +1 tolerance of the true faith |

### Event 3 - Chivalric Order of St. Rastislav (Orthodox only)
Creates a chivalric order with these effects:

| Effect | Value |
|---|---|
| Military ability | +15 |
| Military tactics | +0.15 |
| Prestige | +0.05 |
| Religious influence | +0.10 |

### Event 4 - Opal Mines
*Near Eperjes (Presov) we have found beautiful gems rarely seen in Europe. These opals are truly beautiful, some of them like a crystallized rainbow. If we can mine them, everyone will want a piece.*

**Requirements**
- Controls Eperjes (Presov), or the location just east of it
- Year is 1350 or later
- If the AI declines, the event should become available to other countries

**Effects**
- Changes the location's goods to gems
- Adds a permanent location modifier, "Slovakian Opal Mines": +50% gems output, +0.1% prestige

---

## 8. Implementation notes

These are things to check when building the content. The spec above is unchanged.

**Effects that may not have a direct engine equivalent; check them first**
- "Family member in cabinet gives +5% crown power" (succession law)
- "Score per ability +2.50" (succession law)
- "+20 building slots in towns/cities" (Royal Free Cities). This looks very high; maybe +2 was meant?
- "Can recruit soldiers" on the Hradisko

**Numbers that look off**
- "+0.1% prestige" on the Opal Mines and "+0.05 prestige" on the chivalric order are both very small. Check which unit each value is in.
- Laborer Protection's +33% estate power is unusually strong for a single privilege.

**Event 4:** the "or the tile next to it" fallback needs a specific location picked once you've checked the map.
