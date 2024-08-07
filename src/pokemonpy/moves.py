 #companion to pokemon.py
"""
Copyright (C) 2023 Adarius
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
#normal 0,fire 1,water 2,grass 3,electric 4,ice 5,fighting 6,poison 7,
#ground 8,flying 9,psychic 10,bug 11,rock 12,ghost 13,dragon 14,
#dark 15,steel 16,fairy 17
import numpy as np
def getMoveInfo(moveIndex):
    return mov[moveIndex]
def movers():
    return
## move name // power // accuracy // pp // phys/spec/status // contact? // type // priority // description // code-notes
moremoves=[
        ("V-create",180,95,5,0,1,1,0,"The user ignites its forehead and hurls itself at the target!\nLowers user's Def. Sp.D and Spe. 1 stage each.","stat self,de:sd:sp,-1:-1:-1,100"),

        ("Prismatic Laser",160,100,10,1,0,10,0,"The user attacks the target with lasers using the power of a prism!\nThe user must rest on the next turn.","mustRest"),
        ("Eternabeam",160,90,5,1,0,14,0,"The user harnesses Dynamax energy and releases it in a beam!\nThe user must rest on the next turn.","mustRest"),
        
        ("Hyper Beam",150,90,5,1,0,0,0,"The user attacks with a powerful beam!\nThe user must rest on next turn.","mustRest"),
        ("Giga Impact",150,90,5,0,1,0,0,"The user charges at the target using every bit of its power!\nThe user must rest on next turn.","mustRest"),
        ("Blast Burn",150,90,5,1,0,1,0,"The user razes the target with a fiery explosion!\nThe user must rest on next turn","mustRest"),
        ("Eruption",150,100,5,1,0,1,0,"The user attacks with explosive fury!\nThe lower the user's HP, the lower this move's power.","spout"),
        ("Hydro Cannon",150,90,5,1,0,2,0,"The user attacks the target with a watery blast!\nThe user must rest on next turn.","mustRest"),
        ("Water Spout",150,100,5,1,0,2,0,"The user spouts water to damage the target!\nThe lower the user's HP, the lower this move's power.","spout"), #'spout' = this, eruption, drag energy
        ("Frenzy Plant",150,90,5,1,0,3,0,"The user slams the target with roots from an enormous tree!\nThe user must rest on next turn.","mustRest"),
        ("Chloroblast",150,95,5,1,0,3,0,"The user amasses chlorophyll and launches it at the target!\nThe user loses half of its max HP to recoil damage.","recoil 1/2maxhp"),
        ("Meteor Assault",150,100,5,0,0,6,0,"The user attacks wildly with its thick leek!\nThe user must rest on next turn.","mustRest"),
        ("Rock Wrecker",150,90,5,0,0,12,0,"The user launches a huge boulder at the target!\n The user must rest on next turn.","mustRest bullet"), #bulletproof ability is immune
        ("Head Smash",150,80,5,0,1,12,0,"The user attacks the target with a full-power headbutt!\nThe user takes 1/2 recoil damage.","recoil 1/2"),
        ("Roar of Time",150,90,5,1,0,14,0,"The user shouts a roar that distorts time and inflicts chronological damage on the target!\nThe user must rest on next turn.","mustRest"),
        ("Dragon Energy",150,100,5,1,0,14,0,"The user attacks by converting its life-force into power!\nThe lower the user's HP, the lower this move's power.","spout"),

        ("Boomburst",140,100,10,1,0,0,0,"The user attacks with a terrible, explosive sound!","sound"), #sound move
        ("Psycho Boost",140,90,5,1,0,10,0,"The user attacks with all its might!\nLowers the user's Sp.A 2 stages.","stat self,sa,-2,100"),

        ("Skull Bash",130,100,10,0,1,0,0,"The user tucks its head in and charges at the target!\nTwo-turn move.","2turn skullbash"), #needs to raise defense 1 stage on the prep
        ("Overheat",130,90,5,1,0,1,0,"The user attacks with its full power!\nLowers the user's Sp.A 2 stages.","stat self,sa,-2,100"),
        ("Blue Flare",130,85,5,1,0,1,0,"The user engulfs the target in an beautiful, intense blue flame!\n20% chance to leave a burn.","burn 20"),
        ("Leaf Storm",130,90,5,1,0,3,0,"The user whips up a storm of leaves around the target!\nLowers the user's Sp.A 2 stages.",'stat self,sa,-2,100'),
        ("Draco Meteor",130,90,5,1,0,14,0,"The user calls upon its draconic powers and unleashes a storm of meteors!\nLowers the user's Sp.A 2 stages.","stat self,sa,-2,100"),

        ("Solar Blade",125,100,10,0,1,3,0,"The user focuses sunlight into a blade to attack!\nTwo-turn move, one-turn in harsh sunlight.","2turn solar"),

        #("Tera Starstorm",120,100,5,1,0,0,0,"The user bombards the target with the power of its crystals... \nand eliminates them.","null"),
        ("Double-Edge",120,100,15,0,1,0,0,"The user rushes the target with a reckless tackle!\nThe user takes 1/3 recoil damage.","recoil 1/3"),
        ("Head Charge",120,100,15,0,1,0,0,"The user charges with its head and powerful guard hair!\nThe user takes 1/4 recoil damage.","recoil 1/4"),
        ("Mega Kick",120,75,5,0,1,0,0,"The user launches a kick with muscle-packed power!","null"),
        ("Techno Blast [Normal]",120,100,5,1,0,0,0,"The user fires a beam of light at its target!\nThis is the Normal-type drive.","null"),
        ("Techno Blast [Fire]",120,100,5,1,0,1,0,"The user fires a beam of light at its target!\nThis is the Fire-type drive.","null"),
        ("Techno Blast [Water]",120,100,5,1,0,2,0,"The user fires a beam of light at its target!\nThis is the Water-type drive.","null"),
        ("Techno Blast [Electric]",120,100,5,1,0,4,0,"The user fires a beam of light at its target!\nThis is the Electric-type drive.","null"),
        ("Techno Blast [Ice]",120,100,5,1,0,5,0,"The user fires a beam of light at its target!\nThis is the Ice-type drive.","null"),
        ("Flare Blitz",120,100,15,0,1,1,0,"The user cloaks itself in fire and charges the target!\nThe user takes 1/3 recoil damage, 10% chance to burn, thaws the user if frozen.","recoil 1/3 burn 10 thaws"),
        ("Pyro Ball",120,90,5,0,0,1,0,"The user turns a small stone to a fiery meteor and launches it at the target!\n10% chance to burn, thaws the user if frozen.","burn 10 thaws"),
        ("Wave Crash",120,100,10,0,1,2,0,"The user summons a giant wave and crashes into the target!\nThe user takes 1/3 recoil damage.","recoil 1/3"),
        ("Wood Hammer",120,100,15,0,1,3,0,"The user slams its rugged body into the target!\nThe user takes 1/3 recoil damage.","recoil 1/3"),
        ("Solar Beam",120,100,10,1,0,3,0,"The user focuses sunlight into a beam to attack!\nTwo-turn move, one-turn in harsh sunlight.","2turn solar"),
        ("Volt Tackle",120,100,15,0,1,4,0,"The user electrifies itself and charges the target!\nThe user takes 1/3 recoil damage, 10% chance to paralyze.","recoil 1/3 para 10"),
        ("Zap Cannon",120,50,5,1,0,4,0,"The user fires an eletric blast like a cannon!\n100% chance to paralyze.","para 100"),
        ("Close Combat",120,100,5,0,1,6,0,"The user drops their guard to achieve an all out attack!\nLowers the user's Def. Sp.D 1 stage each.","stat self,de:sd,-1:-1,100"),
        ("Superpower",120,100,15,0,1,6,0,"The user draws on its latent potential and attacks the target with great power!\nLowers the user's Atk. Def. 1 stage each.","stat self,at:de,-1:-1,100"),
        ("Focus Blast",120,70,5,1,0,6,0,"The user heightens its mental focus an unleashs its power!\n10% chance to lower the target's Sp.D 1 stage.","stat targ,sa,-1,10"),
        ("Precipice Blades",120,85,10,0,0,8,0,"The user manifests the power of the land and attacks the target with fearsome blades of stone!","null"),
        ("Brave Bird",120,100,15,0,1,9,0,"The user tucks in its wings and charges at a low altitude!\nThe user takes 1/3 recoil damage.","recoil 1/3"),
        ("Dragon Ascent",120,100,5,0,1,9,0,"The user attacks by dropping out of the sky at high speed! Lowers the user's Def. Sp.D 1 stage each.","stat self,de:sd,-1:-1,100"),
        ("Future Sight",120,100,5,1,0,10,0,"The user looks into the future and predicts an attack!","futuresight"),
        ("Megahorn",120,85,10,0,1,11,0,"The user rams into the target with its tough and impressive horn!","null"),
        ("Shadow Force",120,100,5,0,1,13,0,"The user disappears into the dark and strikes the target on the next turn!","shadowforce 2turn semi-invul"),
        ("Dragon Fist",120,100,5,0,1,14,0,"If the user doesn't do it, who will?\nLowers the user's Spe. 1 stage.","stat self,sp,-1,100"),

        ("Fire Blast",      110,85,5,1,0,1,0,"The user attacks with a blast of all-consuming flames!\n10% chance to burn.","burn 10"),
        ("Origin Pulse",    110,85,10,1,0,2,0,"The user attacks the target with countless beams of glowing blue light!","launching"), #launching = powered by mega-launcher
        ("Hydro Pump",      110,80,5,1,0,2,0,"The user blasts the target with a huge volume of water under great pressure!","null"),
        ("Thunder",         110,70,10,1,0,4,0,"The user drops a wicked lightningbolt on the target to inflict damage!\n30% chance to paralyze.","para 30 thunder"),
        ("Blizzard",        110,70,5,1,0,5,0,"The user summons a howling blizzard to strike the target!\n10% chance to freeze, doesn't miss in hail.","frze 10 blizzard"), #doesn't miss in hail, need to program
        ("Hurricane",       110,70,10,1,0,9,0,"The user wraps its target in a fierce wind from a furious storm!\n30% chance to confuse, doesn't miss in rain.","conf 30 thunder"),
        ("Clanging Scales", 110,100,5,1,0,14,0,"The user rubs the scales on its body and makes a hugh noise to inflict damage on the target!\nLowers the user's Def. 1 stage.","stat self,de,-1,100 sound"),
        
        ("Judgement",       100,100,10,1,0,0,0,"The user pelts the battlefield with bolts of light from the sky!","null"),
        ("Fusion Flare",    100,100,5,1,0,1,0,"The user throws down a giant flame!\nMore powerful if used after Fusion Bolt, thaws the user if frozen.","fusion-f thaws"),
        ("Sacred Fire",     100,95,5,1,0,1,0,"The target is razed with a mystical fire of great intensity!\n50% chance to burn the target, thaws the user if frozen.","thaws burn 50"),
        ("Crabhammer",      100,90,10,0,1,2,0,"The target is hammered with a large pincer!\nIncreased crit' ratio.","highCrit"),
        ("Fusion Bolt",     100,100,5,0,0,4,0,"The user throws down a giant lightning bolt!\nMore powerful if used after Fusion Flare.","fusion-b"),
        ("Earthquake",      100,100,10,0,0,8,0,"The user causes a powerful earthquake!\nPower is halved if used on Grassy Terrain.","nerfGrassy"), #one day we'll generalize moves having their power nerfed under certain conditions....not today tho
        ("Aeroblast",       100,95,5,1,0,9,0,"The user shoots a vortex of air at the target!\nIncreased crit. ratio.","highCrit"),
        ("Psystrike",       100,100,10,1,0,10,0,"The user materializes an odd psychic wave to attack!\nDamage is calculated with the user's Sp.A and the target's Def.","psystrike"), #will use psystrike tag for psyshock and secret sword
        ("Stone Edge",      100,80,5,0,0,12,0,"The user stabs the target from below with sharpened stones!\nIncreased crit' ratio.","highCrit"),
        ("Core Enforcer",   100,100,10,1,0,14,0,"The user unleashes a super sick laser and draws a 'Z'!","null"), #otherwise would suppress abilities, but we have none
        ("Spacial Rend",    100,95,5,1,0,14,0,"The user tears the fabric of space aroud the target!\nIncreased crit' ratio.","null"), #otherwise would suppress abilities, but we have none
        ("Iron Tail",       100,75,15,0,1,16,0,"The user slams the target with a steel-hard tail!\n30% chance to lower target's Def. 1 stage.","stat targ,de,-1,30"),

        ("Heat Wave",   95,90,10,1,0,1,0,"The user exhales hot breath on the target!\n10% chance to burn.","burn 10"),
        ("Moonblast",   95,100,15,1,0,17,0,"The user calls on the power of the Moon to attack the target!\n30% chance to lower the target's Sp.A 1 stage.","stat targ,sa,-1,30"),
        
        ("Flamethrower",90,100,15,1,0,1,0,"The user attacks with a powerful flame!\n10% chance to burn.","burn 10"),
        ("Surf",90,100,15,1,0,2,0,"The user swamps everything around it with a giant wave!","surf"), #hits during dive
        ("Muddy Water",90,85,10,1,0,2,0,"The user attacks by shooting muddy water at the target!\n30% chance to lower the target's Accu..","stat targ,ac,-1,30"),
        ("Aqua Tail",90,90,10,0,1,2,0,"The user swings its tail like a vicious wave in a raging storm!","null"),
        ("Leaf Blade",90,100,15,0,1,3,0,"The user attacks with a sharpened leaf!\nIncreased crit' ratio.","highCrit"),
        ("Thunderbolt",90,100,15,1,0,4,0,"The user attacks with a bolt of lightning!\n10% chance to paralyze.","para 10"),
        ("Ice Beam",90,100,15,1,0,5,0,"The user focuses a stream of ice at the target!\n10% chance to freeze.","frze 10"),
        ("Triple Arrows",90,100,10,0,1,6,0,"The user kicks, then fires three arrows!\nIncreased crit. ratio, 50% chance to lower target's Def. 1 stage, 30% chance to make the target flinch.","highCrit flinch 30 stat targ,de,-1,50"),
        ("Sludge Bomb",90,100,10,1,0,7,0,"Unsanitary sludge is hurled at the target!\n30% chance to poison.","pois 30"),
        ("Earth Power",90,100,10,1,0,8,0,"The user makes the ground under the target erupt with power!\n10% chance to lower target's Sp.D 1 stage.","stat targ,sd,-1,10"),
        ("Thousand Arrows",90,100,10,0,0,8,0,"The user creates arrows from the very ground and hurls them at the target!\nHits ungrounded targets and grounds them.","arrows"),
        ("Fly",90,95,15,0,1,9,0,"The user flies up into the sky, then attacks on the next turn!\nVulnerable to Gust, Smack Down, Sky Uppercut, Thunder, Twister, Hurricane on the first turn.","2turn flying"),
        ("Psychic",90,100,10,1,0,10,0,"The user hits the target with a strong telekinetic force!\n10% chance to lower target's Sp.D 1 stage.","stat targ,sd,-1,10"),
        ("Mystical Power",90,70,10,1,0,10,0,"The user attacks by emitting a mysterious power!\Raises the user's Sp.A 1 stage.","stat self,sa,+1,100"),
        ("Attack Order",90,100,15,0,0,11,0,"The user attacks with a powerful flame! Increased crit' ratio.","highCrit"),
        ("Phantom Force",90,100,10,0,1,13,0,"The user vanishes into another plane, then strikes the target on the next turn!","2turn shadowforce"),
        ("Play Rough",90,90,10,0,1,17,0,"The user attacks by playing rough with the target!\n10% chance to lower the target's Atk. 1 stage.","stat targ,at,-1,10"),
        ("Strange Steam",90,95,10,1,0,17,0,"The user mixes a special steam and shoots it at the target!\n20% chance to confuse.","conf 20"),
        
        ("Blaze Kick",85,90,10,0,1,1,0,"The user attacks with a fiery kick!\n10% chance to burn, increased crit' ratio.","highCrit burn 10"),
        ("Kamehameha",85,100,10,1,0,2,0,"The user concentrates their ki and releases it in a beam!\n50% chance to lower the target's Def. 2 stages.","stat targ,de,-2,50"),
        ("Secret Sword",85,100,10,1,0,6,0,"The user uses odd power to cut with its long horn!\nDamage is calculated with the user's Sp.A and the target's Def.","psystrike"),
        ("Bounce",85,85,5,0,1,9,0,"The user bounces up high on the first turn, then drops onto the target on the next turn!\nVulnerable to Gust, Smack Down, Sky Uppercut, Thunder, Twister, Hurricane on the first turn.","2turn flying para 30"),
        ("Dragon Pulse",85,100,10,1,0,14,0,"The user summons a beastly beam from its mouth!","launching"),
        
        ("Extreme Speed",80,100,5,0,1,0,+2,"The user charges at the target with blinding speed!\nPriority +2.","null"),
        ("Lava Plume",80,100,15,1,0,1,0,"The user torches its surroundings with an inferno of flames!\n30% chance to burn.","burn 30"),
        ("Fire Lash",80,100,15,0,1,1,0,"The user strikes with a burning lash!\nLowers the target's Def. 1 stage.","stat targ,de,-1,100"),
        ("Dive",80,100,10,0,1,2,0,"The user dives on the first turn, then resurfaces to attack on the next turn!\nDouble damage from Surf, Whirlpool on the first turn.","2turn diving"),
        ("Waterfall",80,100,15,0,1,2,0,"The user charges at the target with a wall of water!\n20% chance to make the target flinch.","flinch 20"),
        ("Aqua Step",80,100,10,0,1,2,0,"The user attacks the target with light and fluid dance steps!\nRaises the user's Spe. 1 stage.","stat self,sp,+1,100"),
        ("Aura Sphere",80,100,20,1,0,6,0,"The user looses a blast of aura from deep within its body!\nBypasses accuracy checks.","noMiss"),
        ("Dig",80,100,10,0,1,8,0,"The user burrows into the ground on the first turn, then attacks on the next turn!\nDouble damage from Earthquake, Magnitude, Fissure on the first turn.","2turn digging"),
        ("Zen Headbutt",80,90,15,0,1,10,0,"The user focuses its willpower into its head and attacks the target!\n20% chance to make the target flinch.","flinch 20"),
        ("Psyshock",80,100,10,1,0,10,0,"The user materializes an odd psychic wave to attack!\nDamage is calculated with the user's Sp.A and the target's Def.","psystrike"),
        ("X-Scissor",80,100,15,0,1,11,0,"The user slashes the target by crossing its claws!","null"),
        ("Dragon Claw",80,100,15,0,1,14,0,"The user slashes the target with sharp claws!","null"),
        ("Crunch",80,100,15,0,1,15,0,"The user crunches on the target with sharp fangs!\n20% chance to lower the target's Def. 1 stage.","stat targ,de,-1,20"),
        ("Dark Pulse",80,100,15,1,0,15,0,"The user releases a terrible aura imbued with dark thoughts!\n20% chance to make the target flinch.","flinch 20"),
        ("Flash Cannon",80,100,10,1,0,16,0,"The user gathers all its light energy and releases it all at once at the target!\n10% chance to lower target's Sp.D 1 stage.","stat targ,sd,-1,10"),
        
        ("Crush Claw",75,95,10,0,1,0,0,"The user slashes the target with hard, sharp claws!\n50% chance to lower the target's Def. 1 stage.","stat targ,de,-1,50"), 
        ("Mystical Fire",75,100,10,1,0,1,0,"The user attacks by breathing a special, hot fire!\nLowers the target's Sp.A 1 stage.","stat targ,sa,-1,100"),
        ("Fire Punch",75,100,15,0,1,1,0,"The user hits the target with a fiery punch!\n10% chance to burn.","burn 10"),
        ("Brick Break",75,100,15,0,1,6,0,"The user attacks with a swift chop!\nRemoves Light Screen, Reflect, Aurora Veil from the opponent's side.","breakScreens"),
        ("Air Slash",75,95,15,1,0,9,0,"The user attacks with a blade of air that slices the sky!\n30% chance to make the target flinch.","flinch 30"),
        ("Signal Beam",75,100,15,1,0,11,0,"The user attacks with an odd beam of light!\n10% chance to confuse.","conf 10"),
        
        #("Dizzy Punch",70,100,10,0,1,0,0,"","conf 20"), Why did dizzy punch get kicked out of the game :(
        ("Facade",70,100,20,0,1,0,0,"An attack that does double damage if the user is poisoned, burned, or paralyzed.","facade"),
        ("Retaliate",70,100,5,0,1,0,0,"The user gets revenge for a fainted ally!\nDoubles in power if an ally fainted in the previous turn.","retaliate"),
        ("Headbutt",70,100,15,0,1,0,0,"The user sticks out its head and attacks!\n30% chance to make the target flinch.","flinch 30"),
        ("Aqua Cutter",70,100,20,0,0,2,0,"The user expels pressurized water to cut the target like a blade!\nIncreased crit' ratio.","highCrit"),
        ("Scorching Sands",70,100,10,1,0,8,0,"The user buries the target in searing-hot sand!\n30% chance to burn the target, thaws the user if frozen.","burn 30 thaws thawsTarg"), #thawsTarg is brand new, i believe fire type moves thaw the target by default and this does that because its a hot/burning move but it is not Fire-type so I'll have to work that in gameside
        ("Shadow Claw",70,100,15,0,1,13,0,"The user materializes a sharp claw from the shadows and slashes at the target!\nIncreased crit' ratio.","highCrit"),
        ("Night Slash",70,100,15,0,1,15,0,"The user sneaks in and slashes the target the instant it gets the opportunity!\nIncreased crit' ratio.","highCrit"),
        
        ("Stomp",65,100,20,0,1,0,0,"The user forcefully stomps on the target!\n30% chance to make the target flinch.","flinch 30 noMissMinimize"), #doesn't miss if target used minimize
        ("Fire Fang",65,95,15,0,1,1,0,"The user bites with flame-cloaked fangs!\n10% chance to make the target flinch, 10% chance to burn.","burn 10 flinch 10"),
        ("Bubble Beam",65,100,20,1,0,2,0,"The user forcefully ejects a spray of bubbles at the target!\n10% chance to lower target's Spe. 1 stage.","stat targ,sp,-1,10"),
        ("Octazooka",65,85,10,1,0,2,0,"The user sprays ink in the target's face!\n50% chance to lower the target's Accu. 1 stage.","stat targ,ac,-1,50 bullet"), #bullet-move
        ("Thunder Fang",65,95,15,0,1,4,0,"The user bites with electrified fangs!\n10% chance to make the target flinch, 10% chance to paralyze.","para 10 flinch 10"),
        ("Spark",65,100,20,0,1,4,0,"The user attacks the target with an electrically charged tackle!\n30% chance to paralyze.","para 30"),
        ("Ice Fang",65,95,15,0,1,5,0,"The user bites with frozen fangs!\n10% chance to make the target flinch, 10% chance to freeze.","frze 10 flinch 10"),
        ("Hex",65,100,10,1,0,13,0,"The user attacks relentlessly, doing double damage to a target with status conditions!","hex"),
        ("Ceaseless Edge",65,90,15,0,1,15,0,"The user slashes its shell blade at the target!\nPuts up Spikes on the target's side.","spikes"), #this might not work... i will have to see if we check for spikes tags in damaging moves
        
        ("Swift",60,100,20,1,0,0,0,"The user shoots star-shaped rays at the target!\nBypasses accuracy checks.","noMiss"),
        ("Flame Wheel",60,100,15,0,1,1,0,"The user covers itself in fire and rolls into the target!\n10% chance to burn, thaws the user if frozen.","burn 10 thaws"),
        ("Incinerate",60,100,15,1,0,1,0,"The user attacks with a destructive fire!","null"),#no items to burn up rn
        ("Water Pulse",60,100,20,1,0,2,0,"The user attacks the target with a pulsing blast of water!\n20% chance to confuse.","conf 20"),
        ("Frost Breath",60,90,10,1,0,5,0,"The user blows cold breath on the target!\nThis move always lands a critical hit.","frostbreath"),
        ("Storm Throw",60,100,10,0,1,6,0,"The user strikes the target with a fierce blow!\nThis move always lands a critical hit.","frostbreath"),
        ("Air Cutter",60,95,25,1,0,9,0,"The user launches razor-sharp winds to slash opponents!\nIncreased crit' ratio.","highCrit"),
        ("Silver Wind",60,100,5,1,0,11,0,"The user attacks with powderly scales carried on the wind!\n10% chance to raise all stats 1. stage.","stat self,at:de:sa:sd:sp,1:1:1:1:1,10"), #not in SwSh, but IN LegendsArceus so we move!
        ("Ominous Wind",60,100,5,1,0,13,0,"The user attacks with a mysterious wind.\n10% chance to raise all stats 1 stage.","stat self,at:de:sa:sd:sp,1:1:1:1:1,10"),
        ("Infernal Parade",60,100,15,1,0,13,0,"The user attacks with a myriad of fireballs!\n30% chance to burn, damage is doubled when the target has a status condition.","hex burn 30"),
        #("Feint Attack",60,100,20,0,1,15,0,"",""), uhhh feint attack was nixed in gen 8, and i just programmed night slash so maybes thats a fine replacement?
        ("Bite",60,100,25,0,1,15,0,"The user bites the target with viciously sharp fangs!\n30% chance to make the target flinch.","flinch 30"),
        
        ("Icy Wind",55,95,15,1,0,5,0,"The user attacks with a gust of chilled air!\nLowers the target's Spe. 1 stage.","stat targ,sp,-1,100"),
        ("Acrobatics",110,100,15,0,1,9,0,"The user nimbly strikes the target!","null"), #Im going to just double acrobatics' power bc its canon and we dont have items yet
        
        ("Weather Ball",50,100,10,1,0,0,0,"The user harnesses the power of the weather to attack!\nChanges type and doubles power in non-clear weather.","weatherball"),
        ("Cut",50,95,30,0,1,0,0,"The user cuts the target with a scythe or claw!","null"),
        ("Flame Charge",50,100,20,0,1,1,0,"The user cloaks itself in flames and builds momentum to attack!\nRaises the user's Spe. 1 stage.","stat self,sp,1,100"),
        ("Chilling Water",50,100,20,1,0,2,0,"The user attacks the target with water so cold it saps the target's power!\nLowers target's Atk. 1 stage.","stat targ,at,-1,100"),
        ("Metal Claw",50,95,35,0,1,16,0,"The user rakes the target with steel claws!\n10% chance to raise the user's Atk. 1 stage.","stat self,at,1,10"),
        
        ("Fake Out",40,100,10,0,1,0,+3,"The user hits first and makes the target flinch!\nPriority +3, only works on the first turn after the user enters battle.","flinch 100 fakeout"), #need priority AND first-turn tracking
        ("Quick Attack",40,100,30,0,1,0,+1,"The user lunges at the target so fast it becomes invisible!\nPriority +1.","null"),
        ("Tackle",40,100,35,0,1,0,0,"The user charges to attack!","null"),
        ("Ember",40,100,25,1,0,1,0,"The user attacks with small flames!\n10% chance to burn.","burn 10"),
        ("Aqua Jet",40,100,20,0,1,2,+1,"The user covers itself in water and lunges at the target!\nPriority +1.","null"),
        ("Gust",40,100,35,1,0,9,0,"The user whips up a gust of wind with its wings and launches it at the target!","gust"),
        ("Twister",40,100,20,1,0,14,0,"The user whips up a vicious tornado to tear at the target!\n20% chance to make the target flinch.","gust flinch 20"),
        
        ("Rollout",30,90,20,0,1,12,0,"The user rolls into the target for fives turns!\nDoubles in damage for each consecutive hit.","rollout"),

        #z-moves,                power,accuracy,PP,phys/spec,contact,type,prority,flavor-text,tags
        #("Breakneak Blitz (P)"  ,200,100,1,0,1,0,0,"The user builds momentum using its Z-Power and crashes into the target at full speed!","zmove"),
        #("Breakneak Blitz (S)"  ,200,100,1,1,0,0,0,"The user builds momentum using its Z-Power and crashes into the target at full speed!","zmove"),
        #("Inferno Overdrive (P)",220,100,1,0,1,1,0,"The user breathes a stream of intense fire toward the target using its Z-Power!","zmove"),
        #("Inferno Overdrive (S)",200,100,1,1,0,1,0,"The user breathes a stream of intense fire toward the target using its Z-Power!","zmove"),
        #("Hydro Vortex (P)"     ,180,100,1,0,1,2,0,"The user swallows the target with a huge whirling current using its Z-Power!","zmove"),
        #("Hydro Vortex (S)"     ,200,100,1,1,0,2,0,"The user swallows the target with a huge whirling current using its Z-Power!","zmove"),
        #("Bloom Doom (P)"       ,190,100,1,0,1,3,0,"The user draws energy from the plants and attacks the target with full force using its Z-Power!","zmove"),
        #("Bloom Doom (S)"       ,200,100,1,1,0,3,0,"The user draws energy from the plants and attacks the target with full force using its Z-Power!","zmove"),
        #("Gigavolt Havoc (P)"   ,195,100,1,0,1,4,0,"The user hits the target with an electric current collected by its Z-Power!","zmove"),
        #("Gigavolt Havoc (S)"   ,190,100,1,1,0,4,0,"The user hits the target with an electric current collected by its Z-Power!","zmove"),
        #electric, ice, fighting, poison
        #("Subzero Slammer (P)"  ,200,100,1,0,1,5,0,"The user drops the temperature and freezes the target with its Z-Power!","zmove"),
        #("Subzero Slammer (S)"  ,200,100,1,1,0,5,0,"The user drops the temperature and freezes the target with its Z-Power!","zmove"),
        #("All-Out Pummeling (P)",200,100,1,0,1,5,0,"The user rams an energy orb created by its Z-Power into the target with full force!","zmove"),
        #("All-Out Pummeling (S)",190,100,1,1,0,5,0,"The user rams an energy orb created by its Z-Power into the target with full force!","zmove"),
        #("Acid Downpour (P)"    ,190,100,1,1,0,5,0,"The user sinks the target in a poisonous swamp with its Z-Power!","zmove"),
        #("Acid Downpour (S)"    ,190,100,1,1,0,5,0,"The user sinks the target in a poisonous swamp with its Z-Power!","zmove"),
        #ground 8,flying 9,psychic 10,bug 11,rock 12,ghost 13,dragon 14,
        #dark 15,steel 16,fairy 17


        #max moves
        #("Max Strike (P)",150,100,3,0,1,0,0,"A Normal-type Dynamax move! Decreases the target's Spe. 1 stage.","maxmove stat targ,sp,-1,100"),
        #("Max Strike (S)",150,100,3,1,0,0,0,"A Normal-type Dynamax move! Decreases the target's Spe. 1 stage.","maxmove stat targ,sp,-1,100"),
        #("Max Flare (P)",150,100,3,0,1,1,0,"A Fire-type Dynamax move! Summons harsh sunlight for five turns.","maxmove sun"),
        #("Max Flare (S)",150,100,3,1,0,1,0,"A Fire-type Dynamax move! Summons harsh sunlight for five turns.","maxmove sun"),
        #("Max Geyser (P)",130,100,3,0,1,2,0,"A Water-type Dynamax move! Summons rain for five turns.","maxmove rain"),
        #("Max Geyser (S)",150,100,3,1,0,2,0,"A Water-type Dynamax move! Summons rain for five turns.","maxmove rain"),
        #("Max Overgrowth (P)",140,100,3,0,1,3,0,"A Grass-type Dynamax move! Sprouts grassy terrain for five turns.","maxmove grassy"),
        #("Max Overgrowth (S)",150,100,3,1,0,3,0,"A Grass-type Dynamax move! Sprouts grassy terrain for five turns.","maxmove grassy"),
        #electric, ice, fighting, poison
        #("Max Lightning (P)",140,100,3,0,1,4,0,"An Electric-type Dynamax move! Sparks electric terrain for five turns.","maxmove electric"),
        #("Max Lightning (S)",140,100,3,1,0,4,0,"An Electric-type Dynamax move! Sparks electric terrain for five turns.","maxmove electric"),
        #("Max Hailstorm (P)",140,100,3,0,1,5,0,"An Ice-type Dynamax move! Summons a hailstorm for five turns.","maxmove hail snow"),
        #("Max Hailstorm (S)",140,100,3,1,0,5,0,"An Ice-type Dynamax move! Summons a hailstorm for five turns.","maxmove hail snow"),
        #("Max Knuckle (P)",100,100,3,0,1,6,0,"A Fighting-type Dynamax move! Boosts user's Atk. 1 stage.","maxmove stat self,at,1,100"),
        #("Max Knuckle (S)",100,100,3,1,0,6,0,"A Fighting-type Dynamax move! Boosts user's Atk. 1 stage.","maxmove stat self,at,1,100"),
        #("Max Ooze (P)",95,100,3,0,1,7,0,"A Poison-type Dynamax move! Boosts user's Sp.A 1 stage.","maxmove stat self,sa,1,100"),
        #("Max Ooze (S)",95,100,3,1,0,7,0,"A Poison-type Dynamax move! Boosts user's Sp.A 1 stage.","maxmove stat self,sa,1,100"),
        #ground 8,flying 9,psychic 10,bug 11,rock 12,ghost 13,dragon 14,
        #dark 15,steel 16,fairy 17
        #("Max Quake (P)",140,100,3,0,1,8,0,"A Ground-type Dynamax move! Boosts user's Def. 1 stage.","maxmove stat self,de,1,100"),
        #("Max Quake (S)",130,100,3,1,0,8,0,"A Ground-type Dynamax move! Boosts user's Def. 1 stage.","maxmove stat self,de,1,100"),
        #("Max Airstream (P)",140,100,3,0,1,9,0,"A Flying-type Dynamax move! Boosts user's Spe. 1 stage.","maxmove stat self,sp,1,100"),
        #("Max Airstream (S)",140,100,3,1,0,9,0,"A Flying-type Dynamax move! Boosts user's Spe. 1 stage.","maxmove stat self,sp,1,100"),
        #("Max Mindstorm (P)",130,100,3,0,1,10,0,"A Psychic-type Dynamax move! Weirdly causes psychic terrain for five turns.","maxmove psychic"),
        #("Max Mindstorm (S)",150,100,3,1,0,10,0,"A Psychic-type Dynamax move! Weirdly causes psychic terrain for five turns.","maxmove psychic"),
        #("Max Flutterby (P)",140,100,3,0,1,11,0,"A Bug-type Dynamax move! Lowers target's Sp.A 1 stage.","maxmove stat targ,sa,-1,100"),
        #("Max Flutterby (S)",130,100,3,1,0,11,0,"A Bug-type Dynamax move! Lowers target's Sp.A 1 stage.","maxmove stat targ,sa,-1,100"),
        #("Max Rockfall (P)",150,100,3,0,1,12,0,"A Rock-type Dynamax move! Summons a sandstorm for five turns.","maxmove sand"),
        #("Max Rockfall (S)",140,100,3,1,0,12,0,"A Rock-type Dynamax move! Summons a sandstorm for five turns.","maxmove sand"),
        #("Max Phantasm (P)",140,100,3,0,1,13,0,"A Ghost-type Dynamax move! Lowers target's Def. 1 stage.","maxmove stat targ,de,-1,100"),
        #("Max Phantasm (S)",140,100,3,1,0,13,0,"A Ghost-type Dynamax move! Lowers target's Def. 1 stage.","maxmove stat targ,de,-1,100"),
        #("Max Wyrmwind (P)",140,100,3,0,1,14,0,"A Dragon-type Dynamax move! Lowers target's Atk. 1 stage.","maxmove stat targ,at,-1,100"),
        #("Max Wyrmwind (S)",150,100,3,1,0,14,0,"A Dragon-type Dynamax move! Lowers target's Atk. 1 stage.","maxmove stat targ,at,-1,100"),
        #("Max Darkness (P)",130,100,3,0,1,15,0,"A Dark-type Dynamax move! Lowers target's Sp.D 1 stage.","maxmove stat targ,sd,-1,100"),
        #("Max Darkness (S)",130,100,3,1,0,15,0,"A Dark-type Dynamax move! Lowers target's Sp.D 1 stage.","maxmove stat targ,sd,-1,100"),
        #("Max Steelspike (P)",140,100,3,0,1,16,0,"A Steel-type Dynamax move! Boosts user's Def. 1 stage.","maxmove stat self,de,1,100"),
        #("Max Steelspike (S)",140,100,3,1,0,16,0,"A Steel-type Dynamax move! Boosts user's Def. 1 stage.","maxmove stat self,de,1,100"),
        #("Max Starfall (P)",130,100,3,0,1,17,0,"A Fairy-type Dynamax move! Mystifies a misty terrain for five turns.","maxmove misty"),
        #("Max Starfall (S)",140,100,3,1,0,17,0,"A Fairy-type Dynamax move! Mystifies a misty terrain for five turns.","maxmove misty"),
        #("Max Guard",0,100,3,1,0,10,0," ","maxmove guard? protect? noMiss?noTarg?"),


        
        #counter and mirror coat,
        ("Counter",     1,100,20,0,1,6,-5,"An attack for countering any physical move.\nInflicts on the target double the damage taken by the user.","counter"),
        ("Mirror Coat", 1,100,20,1,0,10,-5,"An attack for countering any special move.\nInflicts on the target double the damage taken by the user.","mirrorcoat"),#]
#moves22 = [
        #status moves
         #weather moves
        ("Sunny Day",  0,100,5,2,0,1,0,"The user calls on the Sun and causes harsh sunlight!","sun noMiss noTarg"),
        ("Rain Dance", 0,100,5,2,0,2,0,"The user disrupts the air pressure and causes rain!","rain noMiss noTarg"),
        ("Hail",       0,100,5,2,0,5,0,"The user summons a cloudy cold front and creates a hailstorm!","hail noMiss noTarg"),
        #("Snowscape", 0,100,5,2,0,5,0,"The user summons a cloudy cold front that produces snow!","snow noMiss noTarg"),
        ("Sandstorm",  0,100,5,2,0,12,0,"The user calls on the local sands to whip up a sandstorm!","sand noMiss noTarg"),
         #terrain moves
        ("Grassy Terrain",   0,100,10,2,0,3,0,"The user covers the battlefield with grass for 5 turns!\nGrass-type moves from grounded Pokémon get a 30% boost, grounded Pokémon heal 1/16 of their max HP each turn, Bulldoze, Earthquake, Magnitude are halved in power.","grassy noMiss noTarg"),
        ("Electric Terrain", 0,100,10,2,0,4,0,"The user electrifies the battlefield for 5 turns!\nElectric-type moves from grounded Pokémon get a 30% boost, grounded Pokémon cannot be put to sleep.","electric noMiss noTarg"),
        ("Psychic Terrain",  0,100,10,2,0,10,0,"The user makes the battlefield weird for 5 turns!\nPsychic-type moves from grounded Pokémon get a 30% boost, grounded Pokémon cannot be hit by priority moves.","psychic noMiss noTarg"),
        ("Misty Terrain",    0,100,10,2,0,17,0,"The user covers the battlefield in mist for 5 turns!\nDragon-type moves targeting grounded Pokémon get a 50% nerf, grounded Pokémon cannot be afflicted with a status confition.","misty noMiss noTarg"),
         #entry hazards
        ("Spikes",        0,100,20,2,0,8,0,"The user spreads spikes on the targets's side of the field!\nStack up to 3 times.","noMiss spikes noTarg"),
        ("Toxic Spikes",  0,100,20,2,0,7,0,"The user sends out toxic barbs on the target's side of the field!\nPokémon are poisoned on entry, stacks up to 2 times for bad poison.","noMiss toxspk noTarg"),
        ("Sticky Web",    0,100,20,2,0,11,0,"The user weaves a web on the target's side of the field!\nLowers Spe. 1 stage upon entry.","noMiss sticky noTarg"),
        ("Stealth Rocks", 0,100,20,2,0,12,0,"The user spreads pointed stones on the targets's side of the field!\nDoes rock-type damge.","noMiss rocks noTarg"),
         #reflect, lightscreen
        ("Aurora Veil",  0,100,20,2,0,5,0,"The user draws on the hail to create a barrier that reduces damage from physical and special attacks for 5 turns!\nFails if it isn't hailing.","veil needHail noTarg"),
        ("Reflect",      0,100,20,2,0,10,0,"The user creates a wall of light that reduces damage from physical attacks for 5 turns!","reflect noMiss noTarg"),
        ("Light Screen", 0,100,20,2,0,10,0,"The user creates a wall of light that reduces damage from special attacks for 5 turns!","lightscreen noMiss noTarg"),
         #healing
        ("Recover",   0,100,10,2,0,0,0,"The user regenerates cells to heal itself by half its max HP.","heals recover noMiss noTarg"),
        ("Aqua Ring", 0,100,20,2,0,2,0,"The user envelops itself with a veil of healing waters.","aquaring noMiss noTarg"),
        ("Synthesis", 0,100,5,2,0,3,0,"The user takes in sunlight to restore HP.\nRestores more HP in harsh sunlight, less in non-sunny, non-clear weather.","heals synthesis noMiss noTarg"),
         #stat(istic) changes
        ("Harden",       0,100,40,2,0,0,0,"The user stiffens the muscles in its body!\nRaises the user's Def. 1 stage.","stat self,de,1 noMiss noTarg"),
        ("Defense Curl", 0,100,40,2,0,0,0,"The user curls up to hide its weak spots!\nRaises the user's Def. 1 stage.","stat self,de,1 noMiss curled noTarg"),
        ("Swords Dance", 0,100,20,2,0,0,0,"The user uplifts the fighting spirit with a frenetic dance!\nRaises the user's Atk. 2 stages.","stat self,at,2 noMiss noTarg"),
        ("Growth",       0,100,20,2,0,0,0,"The user's body grows all at once!\nRaises the user's Atk. Sp.A 1 stage each. Two each in harsh sunlight.","stat self,at:sa,1:1 noMiss growth noTarg"),
        ("Double Team",  0,100,15,2,0,0,0,"The user moves so quick it creates afterimages!\nRaises the user's Evas. 1 stage.","stat self,ev,1 noMiss noTarg"),
        ("Confide",      0,100,20,2,0,0,0,"The user tells the target a (quite inappropriate) secret!\nLowers the target's Sp.A 1 stage.","stat targ,sa,-1 noMiss"),
        ("Growl",        0,100,40,2,0,0,0,"The user growls cutely to disarm the target!\nLowers the target's Atk. 1 stage.","stat targ,at,-1"),
        ("Withdraw",     0,100,40,2,0,2,0,"The user withdraws into its body!\nRaises the user's Def. 1 stage.","stat self,de,1,100 noMiss noTarg"),
        ("Amnesia",      0,100,20,2,0,10,0,"The user empties its mind and forgets its concerns!\Raises the user's Sp.D 2 stages.","stat self,sd,2 noMiss noTarg"),
        ("String Shot",  0,95,40,2,0,11,0,"The user spins silk to bind the target!\nLowers the target's Spe. 1 stage.","stat targ,sp,-1"),
        ("Dragon Dance", 0,100,20,2,0,14,0,"The user vigorously performs a mystic, poweful dance!\nRaises the user's Atk. Spe. 1 stage each.","stat self,at:sp,1:1 noMiss noTarg"),
        ("Nasty Plot",   0,100,20,2,0,15,0,"The user stimulates the brain by thinking bad thoughts!\nRaises the user's Sp.A 2 stages.","stat self,sa,2 noMiss noTarg"),
        ("Metal Sound",  0,85,40,2,0,16,0,"The user creates horrible metal-scraping sounds to unnerve the target!\nLowers the target's Sp.D 2 stages.","stat targ,sd,-2"), #sound-based, soundproof ability is immune,
        ("Geomancy",     0,100,10,2,0,17,0,"The user absorbs energy from its surroundings and powers up on the next turn!\nRaises the user's Sp.A Sp.D Spe. 2 stages each. Two-turn move.","stat self,sa:sd:sp,2:2:2 noMiss 2turn geomance noTarg"),
         #stat(us) conditions
        ("Will-O-Wisp",   0,85,15,2,0,1,0,"The user shoots a sinister flame to burn the target!","burn 100"),
        ("Stun Spore",    0,75,30,2,0,3,0,"The user releases spores that paralyze the target!","para 100 typeImmune grass"), #typeImmune for poke types with immunities
        ("Sleep Powder",  0,75,15,2,0,3,0,"The user uses a powder to lull the target to sleep!","sleep 100 typeImmune grass"),
        ("Poison Powder", 0,75,35,2,0,7,0,"The user creates a powder to poison the target!","pois 100 typeImmune grass"),
        ("Toxic",         0,90,10,2,0,7,0,"The user badly poisons the target!","badPois 100 noMissPoisons"), #doesn't miss if used by a poison-type
        ("Confuse Ray",   0,100,10,2,0,13,0,"The user lets loose a sinister beam that causes confusion!","conf 100"),
        #to do: z/max moves! terrain pulse! brine! trapping/binding moves!
        ("Struggle", 50,100,1,0,1,18,0,"The user is otherwise out of moves!","noMiss recoil 1/4maxhp")
        ]
#constructing dtypes and names to accompany data
labels = np.dtype( [('name','U25'),('pwr','i4'),('accu','i4'),('pp','i4'),('special?','i4'),('contact?','i4'),('type','i4'),('priority','i4'),('desc','U280'),('notes','U140')] )
mov = np.array(moremoves, dtype=labels)
new_dt = np.dtype( [('index','i4')] + mov.dtype.descr)
mov2 = np.zeros(mov.shape, dtype=new_dt)
#creating structed arrays
#new dtype to add the index column and priority 
#new structured array for the new dtype
#dump data from old array into new array
for i in mov.dtype.names:
    mov2[i] = mov[i]
    pass
mov = mov2
mov['index'] = np.arange(0,len(mov), dtype=int)
#find struggle, future sight, tackle
ind=np.argwhere(mov["name"]=="Struggle")
struggle=int(mov[ind]["index"])
ind2 = np.argwhere(mov["name"]=="Future Sight")
futuresigh=int(mov[ind2]["index"])
tackl = int(mov[int(np.argwhere(mov["name"]=="Tackle"))]["index"])
### find the max and z moves, keep their indices stored somewhere so as to easily exclude them ###
maxx = [ "maxmove" in i for i in mov['notes'] ]
max2 = np.argwhere( maxx )
maxset = [ i[0] for i in max2 ]
zzzs = [ "zmove" in i for i in mov['notes'] ]
zzz2 = np.argwhere( zzzs )
zzzset = [ i[0] for i in zzz2 ]
### xx ###

#Natures?
#no idea the best way to store this data
#okay got it
#atk = 0, def = 1, spatk = 2, spdef = 3, speed = 4
natures = [ ["Hardy","Lonely","Adamant","Naughty","Brave"], \
           ["Bold","Docile","Impish","Lax","Relaxed"], \
               ["Modest","Mild","Bashful","Rash","Quiet"],\
                   ["Calm","Gentle","Careful","Quirky","Sassy"], \
                       ["Timid","Hasty","Jolly","Naive","Serious"] ]
natures = np.array(natures,dtype=object)
#
if __name__ == "__main__":
    np.save("saved_movedex.npy",mov)
    #np.save("saved_natures.npy",natures)
else:
    pass

