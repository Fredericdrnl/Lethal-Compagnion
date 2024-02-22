-- speed setup of BDD (just ctrl C and ctrl V this file).
CREATE TABLE Monsters(
    id_monster SERIAL PRIMARY KEY,
    underscore VARCHAR(50),
    name_monster VARCHAR(50),
    entry_monster VARCHAR(500),
    particularity VARCHAR(500),
    strategy VARCHAR(500),
    picture_monster VARCHAR(500)
);

CREATE TABLE Scraps(
    id_scrap SERIAL PRIMARY KEY,
    underscore VARCHAR(500),
    name_scrap VARCHAR(500),
    entry_scrap VARCHAR(500),
    min_cost_scrap INTEGER,
    max_cost_scrap INTEGER,
    weight_scrap INTEGER,
    conductive_scrap BOOLEAN,
    two_handed BOOLEAN,
    picture_scrap VARCHAR(500)
);

CREATE TABLE Moons(
    id_moon SERIAL PRIMARY KEY,
    name_moon VARCHAR(500),
    difficulty VARCHAR(500),
    cost_moon INTEGER,
    weather VARCHAR(500),
    default_layout VARCHAR(500),
    min_scrap INTEGER,
    max_scrap INTEGER,
    picture_moons VARCHAR(500)
);

CREATE TABLE Store(
    id_store SERIAL PRIMARY KEY,
    underscore VARCHAR(5000),
    name_store VARCHAR(500),
    entry_store VARCHAR(500),
    cost_store INTEGER,
    weight_store INTEGER,
    conductive_store VARCHAR(500),
    battery_store VARCHAR(500),
    picture_store VARCHAR(500)
);

INSERT INTO Monsters (id_monster,underscore,name_monster,entry_monster,particularity,strategy,picture_monster) VALUES
(1,'Eyeless_Dog', 'Eyeless Dog','Eyeless Dogs, colloquially known as just Dogs, are large aggressive pack hunters that roam outdoors.','Blind, Exceptional Hearing','Be Quiet','https://static.miraheze.org/lethalwiki/thumb/1/1e/Eyelessdogsrender.png/150px-Eyelessdogsrender.png'),
(2,'Baboon_Hawk', 'Baboon Hawk','Baboon Hawks are a primate of the family Cercopithecidae. They are hunchbacked but can stand up to 8 feet on average.','','Try to make trips to/from The Ship in groups. They won t attack players unless they outnumber them','https://static.miraheze.org/lethalwiki/thumb/4/4d/Baboonhawkrender.png/150px-Baboonhawkrender.png'),
(3,'Circuit_Bees', 'Circuit Bees','Circuit Bees are highly defensive. They will leave the nest to attack any creature that comes within several meters','','Taking a Circuit Bees hive is almost always worth it if you have time, as it is valued at around 100','https://static.miraheze.org/lethalwiki/thumb/e/e2/Circuitbees.png/405px-Circuitbees.png'),
(4,'Manticoil', 'Manticoil','Manticoils are passive ambient birds found outdoors.','','They re useless','https://static.miraheze.org/lethalwiki/thumb/c/cd/Manticoils.png/405px-Manticoils.png'),
(5,'Roaming_Locusts', 'Roaming Locusts','Roaming Locusts are small harmless insects found outdoors in a spherical swarm.','','They re useless','https://static.miraheze.org/lethalwiki/thumb/0/03/Roaminglocusts.png/405px-Roaminglocusts.png'),
(6,'Earth_Leviathan', 'Earth Leviathan','They seem to behave as predators. It s speculated they can burrow as far as 40 meters underground, judging by the incredible excavations they can leave behind.','Earth Leviathans will spawn during Nighttime on moons in which they appear, burrowed in the ground.','The presence of an Earth Leviathan can be ascertained by listening for underground groaning sounds and avoid staying too close to your teammates ','https://static.miraheze.org/lethalwiki/thumb/7/72/Earthleviathanrender.png/114px-Earthleviathanrender.png'),
(7,'Forest_Keepers', 'Forest Keepers','Forest Keepers, colloquially known as Giants, are enormous hostile entities found roaming outdoors.','Not a good view','Staying crouched, silent','https://static.miraheze.org/lethalwiki/thumb/6/60/Forestkeeperrender.png/143px-Forestkeeperrender.png'),
(8,'Bracken', 'Bracken','The Bracken, or sometimes called Flowerman, is a dangerous entity in lethal company.','Brackens have 3 possible states: sneaking, evading, and enraged.','Zap guns are effective against Brackens, making them possible to kill if paired with a player holding a shovel.','https://static.miraheze.org/lethalwiki/thumb/0/0e/Brackenrender.png/120px-Brackenrender.png'),
(9,'Bunker_Spider', 'Bunker Spider','Bunker Spiders produce silk and lay it around their chosen nesting area, then wait for it to be tripped on. They can be seen waiting on walls, often over doorways where prey could enter unaware','The Bunker Spider will not attack while it s in its preparation phase, during which it will place webs within its territory',' a player can easily walk past spider territory if they ve arrived early enough.','https://static.miraheze.org/lethalwiki/thumb/9/94/Bunkerspiderrender.png/150px-Bunkerspiderrender.png'),
(10,'Coil_Head', 'Coil-Head','Coil-Heads visual appearance is that of a bloody mannequin with its head connected by a spring','can only move when it is outside the line of sight of every player','One member keep watch on it as others loot','https://static.miraheze.org/lethalwiki/thumb/d/dd/Coil_head_3d.webp/112px-Coil_head_3d.webp.png'),
(11,'Hoarding_Bug', 'Hoarding Bug','They are large, social insects. While often found living alone, they have been found to share their nests with members of their own species','Hoarding Bugs are skittish by default and will not attack players until provoked. They will search the map for scrap and bring it back to a pre-defined nest area','Trade items with them','https://static.miraheze.org/lethalwiki/thumb/d/da/Hoardingbugrender.png/62px-Hoardingbugrender.png'),
(12,'Hygrodere', 'Hygrodere','Hygrodere are drawn to heat and oxygen and can detect it from seemingly anywhere','A Hygrodere will move extremely slowly around the map','Just run faster','https://static.miraheze.org/lethalwiki/thumb/b/b2/LC_Hygrodere.webp/150px-LC_Hygrodere.webp.png'),
(13,'Jester', 'Jester','You cant hide from it, just evacuate THERE S NO FREAKING SCIENTIFIC RECORD','The Jester initiates a random timer, varying from 12 to 28 seconds, which determines the duration before it switches to its cranking state','When its cranking or chasing begins, players should immediately get to the exit','https://static.miraheze.org/lethalwiki/thumb/e/e0/Jesterrender.png/62px-Jesterrender.png'),
(14,'Nutcracker', 'Nutcracker','The guardians of the house.','The Nutcracker spawns carrying a Shotgun','Killing Nutcrackers is almost always worth it due to the power of the shotgun','https://static.miraheze.org/lethalwiki/thumb/b/be/Nutcrackerrender.png/115px-Nutcrackerrender.png'),
(15,'Snare_Flea', 'Snare Flea','The Snare Flea thrives in dark, warm areas','Snare Fleas wait on the ceiling of any room/corridor. Once a player is within range or below, they will proceed to wrap around their head, obstructing their view, muffling and distorting their voice','They die in 2 Shovel hits','https://static.miraheze.org/lethalwiki/thumb/2/26/Snareflearender.png/80px-Snareflearender.png'),
(16,'Spore_lizards', 'Spore lizards','Spore Lizards have a very timid temperament, avoiding confrontation if at all possible','Spore Lizards are passive entities, only attacking players when threatened or cornered','Best option is to simply respect it and leave it alone','https://static.miraheze.org/lethalwiki/thumb/8/8e/Sporelizardrender.png/150px-Sporelizardrender.png'),
(17,'Thumper', 'Thumper','They are deaf and rely entirely on sight','Just dangerous','They take 4 Shovel hits to kill and kill an employee in 3 quick bites','https://static.miraheze.org/lethalwiki/thumb/3/38/Thumperrender.png/134px-Thumperrender.png'),
(18,'Ghost_Girl','Ghost Girl','Cannot currently be scanned','The Ghost Girl is one of the most consistently difficult threats a team can face. She is unique in that, once spawned in, there is no way to avoid interacting with her; she will always pick one employee to haunt.','only one player is affected at a time','https://static.miraheze.org/lethalwiki/thumb/a/ad/Ghostgirlrender.png/123px-Ghostgirlrender.png');

INSERT INTO Moons (id_moon,name_moon,difficulty,cost_moon,weather,default_layout,min_scrap,max_scrap,picture_moons) VALUES
(1,'41-Experimentation','B',0,'Rainy, Stormy, Foggy, Flooded, Eclipsed','Factory',8,11,'https://static.miraheze.org/lethalwiki/thumb/b/b8/Experimentation_map_outside.png/405px-Experimentation_map_outside.png'),
(2,'220-Assurance','D',0,'Rainy, Stormy, Flooded, Eclipsed','Factory',13,16,'https://static.miraheze.org/lethalwiki/thumb/2/2e/Assurancemap.png/405px-Assurancemap.png'),
(3,'56-Vow','C',0,'Flooded, Stormy, Foggy, Eclipsed','Factory',10,12,'https://static.miraheze.org/lethalwiki/thumb/7/7a/Vow.png/405px-Vow.png'),
(4,'21-Offense','B',0,'Rainy, Stormy, Eclipsed, Flooded','Factory',14,17,'https://static.miraheze.org/lethalwiki/thumb/5/56/Offense.png/405px-Offense.png'),
(5,'61-March','B',0,'Flooded, Stormy, Foggy, Eclipsed','Factory',13,16,'https://static.miraheze.org/lethalwiki/thumb/6/6f/March.png/405px-March.png'),
(6,'85-Rend','A',550,'Stormy, Eclipsed','Mansion',18,25,'https://static.miraheze.org/lethalwiki/thumb/7/74/Rend_Map.png/405px-Rend_Map.png'),
(7,'7-Dine','S',600,'Flooded, Eclipsed','Mansion',20,27,'https://static.miraheze.org/lethalwiki/thumb/c/ce/Dine_Map.png/405px-Dine_Map.png'),
(8,'8-Titan','S+',700,'Stormy, Foggy, Eclipsed','Factory',23,37,'https://static.miraheze.org/lethalwiki/thumb/f/f9/Titanmap.png/405px-Titanmap.png');

INSERT INTO Scraps (id_scrap,underscore,name_scrap,entry_scrap,min_cost_scrap,max_cost_scrap,weight_scrap,conductive_scrap,two_handed,picture_scrap) VALUES
(1,'Air_Horn','Air Horn','A red and blue air horn, with a yellow label reading “AIRY BLAST”. Produces a loud sound when used that can be heard by other players and nearby wildlife.',52,72,0,false,false,'https://static.miraheze.org/lethalwiki/thumb/4/42/Airhorn.png/405px-Airhorn.png'),
(2,'Apparatus', 'Apparatus','The Apparatus, or Apparatice as it s called in-game, is a valuable glowing power cell providing energy to the Facility. It always spawns in a dedicated generator room in a Facility. Collecting it will permanently disable Facility power, making escape more difficult: all lights turn off, all bunker doors are forced open and can t be closed anymore. Additionally, collecting the Apparatus has a 70% chance of increasing the interior enemy spawn rate.',80,80,31,true,true,'https://static.miraheze.org/lethalwiki/e/ee/Apparatus.png'),
(3,'Bee_Hive', 'Bee Hive','The Bee Hive is home to Circuit Bees.',50,156,0,true,true,'https://static.miraheze.org/lethalwiki/thumb/3/3c/Beehive.png/405px-Beehive.png'),
(4,'Bottles', 'Bottles','A red box with blue bottles inside.',44,56,19,false,true,'https://static.miraheze.org/lethalwiki/3/32/Bottles.png'),
(5, 'Brass_Bell', 'Brass Bell','A brass bell with a silver handle on top.',48,80,24,true,false,'https://static.miraheze.org/lethalwiki/0/05/Brass_Bell.png'),
(6,'Candy', 'Candy','Hmmm YUMMY !',6,36,11,false,false,'https://static.miraheze.org/lethalwiki/1/1c/Candy.png'),
(7, 'Cash_Register', 'Cash Register','A vintage cash register. Its drawer can be opened and closed, producing a loud sound audible to nearby players and wildlife.',80,160,84,true,true,'https://static.miraheze.org/lethalwiki/thumb/6/6f/Cash_Register.png/405px-Cash_Register.png'),
(8, 'Chemical_Jug', 'Chemical Jug','Yellow barrel similar to a propane tank. This item is exclusive to Vow, and is a relatively high-value two handed item for where it is found.',32,84,32,false,true,'https://static.miraheze.org/lethalwiki/a/a2/Chemical_Jug.png'),
(9, 'Clow_Horn', 'Clow Horn','Produces a honking sound when used that can be heard by other players and nearby wildlife.',52,72,0,true,false,'https://static.miraheze.org/lethalwiki/thumb/5/52/Clown_Horn.png/405px-Clown_Horn.png'),
(10, 'Coffee Mug', 'Coffee Mug','WOMEN ! HAHAHAHA !! SLUUUUURRRPP !',24,68,5,false,false,'https://static.miraheze.org/lethalwiki/7/7f/Coffee_Mug.png'),
(11, 'Comedy_Mask', 'Comedy Mask','The Tragedy and Comedy Masks are a plastic or ceramic Theater tragedy/comedy mask added in version 45. While being used, the employee will hold the mask up to their face, however the Tragedy Mask won t be able to be removed afterwards. While held up to your face, every 5 seconds there is a 65% chance that the mask will possess the employee holding it, turning them into a Masked.',28,52,11,false,false,'https://static.miraheze.org/lethalwiki/e/ed/Comedy.jpg'),
(12, 'Cookie_Mold_Pan', 'Cookie Mold Pan','LET HIM COOK !!!',12,40,16,false,false,'https://static.miraheze.org/lethalwiki/thumb/4/46/Cookie_Mold_Pan.png/405px-Cookie_Mold_Pan.png'),
(13, 'Dustpan', 'Dustpan','A dust pan with a gray handle. Exclusive to Experimentation. Though it weighs nothing, dustpans are very low value, only higher than the lowest values in the game, ie. metal sheets and whoopie cushions.',12,32,0,false,false,'https://static.miraheze.org/lethalwiki/thumb/0/00/Dustpan.png/405px-Dustpan.png'),
(14, 'Egg_Beater', 'Egg Beater','An egg beater with a black handle.',12,44,11,true,false,'https://static.miraheze.org/lethalwiki/0/0a/Egg_Beater.png'),
(15, 'Fancy_Lamp', 'Fancy Lamp','A golden, two-handed lamp with a red top shade. Emits light when on the ground or held. Commonly found in the Mansion.',60,128,21,true,true,'https://static.miraheze.org/lethalwiki/thumb/f/fd/Fancy_Lamp.png/405px-Fancy_Lamp.png'),
(16, 'Flask', 'Flask','The flask was a new item introduced in Version 45 of the game. Visually, the Flask bears a resemblance to a Florence flask.',16,44,19,true,false,'https://static.miraheze.org/lethalwiki/9/92/Flask_round.png'),
(17, 'Gift', 'Gift','The Gift is a scrap item that can be opened to reveal a random scrap item inside. The dropped item is usually worth more than standard scrap, with a min value increased by 10 and a max value increased by 14. The item that spawns from the present is chosen from the scrap pool of the moon it was found on.',12,28,19,false,false,'https://static.miraheze.org/lethalwiki/thumb/2/24/Gift.png/405px-Gift.png'),
(18, 'Gold_Bar', 'Gold Bar','A very rare, very heavy bar of gold. It has the highest possible value of any item in the game, and despite it s weight only being beaten by cash registers, it is a one-handed item. Exclusive to Experimentation and March.',102,210,77,true,false,'https://static.miraheze.org/lethalwiki/4/4e/Gold_Bar.png'),
(19, 'Golden_Cup', 'Golden Cup','A golden chalice adorned with red gemstones. Can only be found on paid moons.',40,80,16,false,false,'https://static.miraheze.org/lethalwiki/d/d9/Golden_Cup.png'),
(20, 'Hair_Brush', 'Hair Brush','I m sorry for you if you can t use it...',8,36,11,false,false,'https://static.miraheze.org/lethalwiki/c/ce/Hair_Brush.png'),
(21, 'Hairdryer', 'Hairdryer','A pink portable hairdryer. When used, it will produce a loud sound and consumes 1/10th of its power from its internal battery. This sound can be detected by nearby players and wildlife.',60,100,7,false,false,'https://static.miraheze.org/lethalwiki/thumb/e/ed/Hairdryer.png/405px-Hairdryer.png'),
(22, 'Homemade_Flashbang', 'Homemade Flashbang','Pulling a pin will cause it to explode immediately, flashing everything in the vicinity, but also dealing minor damage to player that was holding it. Contrary to the stun grenade, it cannot be thrown.',10,28,5,false,false,'https://static.miraheze.org/lethalwiki/d/d6/Homemadeflash.png'),
(23, 'Jar_of_Pickles', 'Jar of Pickles','Three green pickles in a translucent jar with a tan lid. According to rough calculations, the jar presses on your hand with a pressure of 156 Pa (~17 kg),.',32,60,16,false,false,'https://static.miraheze.org/lethalwiki/0/05/Jar_Of_Pickles.png'),
(24, 'Large_Axle','Large Axle','It s a big axle.',36,56,16,true,true,'https://static.miraheze.org/lethalwiki/thumb/8/88/Large_Axle.png/405px-Large_Axle.png'),
(25,'Large_Bolt', 'Large Bolt','Despite its name, the Big Bolt appears to be a large screw.',20,32,19,true,false,'https://static.miraheze.org/lethalwiki/6/63/Large_Bolt.png'),
(26,'Laser_Pointer', 'Laser Pointer','Emits a small red light. Has an estimated range of 20m. Impractical use for navigation but it can be used to check for fall hazards. Laser Pointers are obscured by fog, steam, blizzards, and toxic fumes, with 2 minutes and 20 seconds of battery life.',32,100,0,true,false,'https://static.miraheze.org/lethalwiki/thumb/7/7d/Laser_Pointer.png/405px-Laser_Pointer.png'),
(27, 'Magic_7_Ball', 'Magic 7 Ball','A play on the iconic toy series, Magic 8 Ball. Despite its name, it has no magical properties. Can only be found on paid moons.',36,72,16,false,false,'https://static.miraheze.org/lethalwiki/7/7c/Magic_7_Ball.png'),
(28, 'Magnifying_Glass', 'Magnifying Glass','Large magnifying glass.',44,60,11,false,false,'https://static.miraheze.org/lethalwiki/thumb/5/5f/Magnifying_Glass.png/405px-Magnifying_Glass.png'),
(29, 'Metal_Sheet', 'Metal Sheet','Metal sheet.',10,22,26,true,false,'https://static.miraheze.org/lethalwiki/0/01/MetalSheet.png'),
(30, 'Old_Phone', 'Old Phone','A black satellite phone. When held, it can randomly play garbled static or a loud shrieking sound that can be heard by other players and nearby wildlife. This noise can be heard by Eyeless Dogs.',48,64,5,false,false,'https://static.miraheze.org/lethalwiki/2/2e/Old_Phone.png'),
(31, 'Painting', 'Painting','This is ART (but i don t understand it...),',60,124,32,false,true,'https://static.miraheze.org/lethalwiki/thumb/e/ea/Painting.png/405px-Painting.png'),
(32,'Perfume_Bottle', 'Perfume Bottle','I smell GOOOOD now !',48,104,0,false,false,'https://static.miraheze.org/lethalwiki/f/f5/Perfume_Bottle.png'),
(33, 'Pill_Bottle', 'Pill Bottle','The Pill Bottle is a distinct in-game item characterized by its orange hue and white cap. Although small, inspecting the texture of the prescription label appears to read hello stranger on the top and Dr. what what is this on the bottom. This item exclusively appears on Hard moons, specifically Rend, Dine, and Titan. Notably, Titan stands out as the more prevalent location for encountering the Pill Bottle, being four times as likely as the aforementioned moons.',16,40,0,false,false,'https://static.miraheze.org/lethalwiki/a/a6/Pill_Bottle.png'),
(34, 'Plastic_Fish', 'Plastic Fish','Small light blue fish.',28,40,0,false,false,'https://static.miraheze.org/lethalwiki/a/a4/Plastic_fish.png'),
(35, 'Player_Body', 'Player Body','When a player dies (in most cases),, they leave behind a body which can be recovered through the use of a teleporter or by carrying it back to the ship. However, after players respawn, their bodies will disappear, meaning that bodies cannot be transported between moons. For each dead player, you can obtain their body before leaving the moon, so called bodies recovered. If the body was not obtained, you lose 20% of your current credits for each body. Otherwise, you lose 8% of current credits.',5,5,11,false,true,'https://tse3.mm.bing.net/th?id=OIP.fqKILlC0S_39uDVe3CgUSAHaDy&pid=Api'),
(36, 'Red_Soda', 'Red Soda','A red can, similar to Coca-Cola, with a white label reading SODA.',18,90,7,true,false,'https://static.miraheze.org/lethalwiki/0/0d/Red_Soda.png'),
(37,'Remote', 'Remote','Turns lights on and off in ship when activated.',20,48,0,false,false,'https://static.miraheze.org/lethalwiki/a/a3/Remote.png'),
(38,'Robot_Toy', 'Robot Toy','Continuously makes loud toy noises wqhen picked up. Can be picked up for a 25% chance of disabling the noise. There is a 5% chance that the Robot Toy will frown instead of sporting the typical smile when picked up or switched to from the inventory. When this happens, the robot will not make any noise regardless of the aforementioned 25% chance. This noise can be heard by Eyeless Dogs.',56,88,21,true,false,'https://static.miraheze.org/lethalwiki/thumb/6/63/Robot_Toy.png/405px-Robot_Toy.png'),
(39, 'Rubber_Duckie', 'Rubber Duckie','A yellow rubber duck. Makes a quacking noise when picked up, detectable by other players and nearby wildlife.',2,100,0,false,false,'https://static.miraheze.org/lethalwiki/thumb/a/aa/Rubber_Duckie.png/405px-Rubber_Duckie.png'),
(40, 'Shotgun', 'Shotgun','The Shotgun is an item wielded by the Nutcracker. It will drop once it is killed, along with however many shells the nutcracker had in the shotgun when it died, with 2 extra shells dropped alongside it.The Shotgun deals up to 5 damage at close range, with fall off depending on the distance from the target. This is enough to kill almost every damageable enemy in the game, with the exceptions of Eyeless Dogs being extremely difficult to hit.',30,90,16,false,false,'https://static.miraheze.org/lethalwiki/thumb/6/61/Shotgun.png/405px-Shotgun.png'),
(41,'Shotgun_Shell', 'Shotgun Shell','Ammunition (referred to in-game as Ammo), is a consumable item in the game, exclusively dropped from Nutcrackers. It becomes available for collection after defeating a Nutcracker. The primary function of Ammo is to facilitate reloading the Shotgun while held in your inventory when there is space for it in the shotgun, the sole ranged weapon featured in the game, consuming the shell. Notably, Ammo is consistently generated in pairs upon the Nutcracker s defeat.',0,0,0,false,false,'https://static.miraheze.org/lethalwiki/8/89/Screenshot_2023-12-13_12.40.09_PM.png'),
(42,'Steering_Wheel', 'Steering Wheel','A small steering wheel.',16,32,16,false,false,'https://static.miraheze.org/lethalwiki/thumb/5/5f/Steering_Wheel.png/405px-Steering_Wheel.png'),
(43,'Stop_Sign', 'Stop Sign','A scrap item able to be used to hit and damage certain enemies. Similar to the Shovel or Yield Sign. While it is heavier than the Shovel, it can still be used as an effective weapon.',20,52,21,true,false,'https://static.miraheze.org/lethalwiki/thumb/b/b7/Stop_Sign.png/405px-Stop_Sign.png'),
(44,'Tea_Kettle', 'Tea Kettle','A metal tea kettle, moderately heavy but valuable.',32,56,21,true,false,'https://static.miraheze.org/lethalwiki/thumb/1/14/Tea_Kettle.png/405px-Tea_Kettle.png'),
(45,'Teeth', 'Teeth','Continuously makes chattering noises when picked up. Can be picked up for a 18% chance of disabling the noise. This noise can be heard by Eyeless Dogs.',60,84,0,false,false,'https://static.miraheze.org/lethalwiki/thumb/7/72/Teeth.png/405px-Teeth.png'),
(46, 'Toothpaste', 'Toothpaste','The Toothpaste item is an exclusive commodity found on the most challenging 3 moons within the game. Distinguished by its weightlessness, the Toothpaste item registers at 0lb on the scale. Visually, the Toothpaste item adopts a distinctive appearance, presenting as a red and blue decorated toothpaste container adorned with the inscription CAVITY FIGHTER. Despite what you might think, the item is not consumable.',14,48,0,false,false,'https://static.miraheze.org/lethalwiki/6/61/Toothpaste.png'),
(47, 'Toy_Cube', 'Toy Cube','The Toy Cube stands out as a prevalent one-handed item within the game s item-pool. Notably lightweight, the Toy Cube carries a negligible weight of 0lb, contributing to its ease of use and portability. Visually, it resembles an unsolvable Rubik s Cube. An interesting characteristic of the Toy Cube is its exclusion from the pool of items available for Experimentation, despite its status as one of the more common one-handed items.',24,44,0,false,false,'https://static.miraheze.org/lethalwiki/d/dd/Toy_Cube.png'),
(48, 'Tragedy_Mask', 'Tragedy Mask','The Tragedy and Comedy Masks are a plastic or ceramic Theater tragedy/comedy mask added in version 45. While being used, the employee will hold the mask up to their face, however the Tragedy Mask won t be able to be removed afterwards. While held up to your face, every 5 seconds there is a 65% chance that the mask will possess the employee holding it, turning them into a Masked.',28,52,11,false,false,'https://static.miraheze.org/lethalwiki/b/b2/Tragedy.png'),
(49, 'V-Type_Engine', 'V-Type Engine','A good start to build your own vehicule !',20,56,16,true,true,'https://static.miraheze.org/lethalwiki/6/61/VType.png'),
(50, 'Wedding_Ring', 'Wedding Ring','Will you marry me ?',52,80,16,true,false,'https://static.miraheze.org/lethalwiki/f/fe/Wedding_Ring.png'),
(51, 'Whoopie_Cushion', 'Whoopie Cushion','The Whoopie Cushion stands out as a unique (and amusing), item. Functioning like any standard item, players can locate and acquire it during gameplay. Notably, the Whoopie Cushion holds no weight within the inventory, making it easier to transport. Upon being walked over, the Whoopie Cushion emits a distinctive fart sound. It s essential to note that players are unable to activate the fart sound voluntarily when the item is held, it must be dropped and walked over.',6,20,0,true,false,'https://static.miraheze.org/lethalwiki/a/ae/Whoopie.png'),
(52, 'Yield_Sign', 'Yield Sign','A scrap item able to be used to hit and damage certain enemies. Similar to the Stop Sign or Shovel but much heavier so as practical. This is the heaviest melee weapon of the game.',18,36,42,true,false,'https://static.miraheze.org/lethalwiki/thumb/b/b7/Yield_Sign.png/405px-Yield_Sign.png');

INSERT INTO Store (id_store,underscore,name_store,entry_store,cost_store,weight_store,conductive_store,battery_store,picture_store) VALUES
(1, 'Boombox', 'Boombox','Boomboxes are portable music players that emit a selection of five different songs',60,16,'NO','YES','https://static.miraheze.org/lethalwiki/thumb/8/84/Boombox_Icon.png/150px-Boombox_Icon.png'),
(2, 'Extension Ladder', 'Extension Ladder','The extension ladder can reach as high as nine meters',60,0,'YES','NO','https://static.miraheze.org/lethalwiki/thumb/0/04/Extension_Ladder_Icon.png/150px-Extension_Ladder_Icon.png'),
(3, 'Flashlight', 'Flashlight','Flashlights are tools that emit light in a conical shape in front of the player, aiding exploration. Fully charged flashlights last for 140 seconds.',15,0,'NO','YES','https://static.miraheze.org/lethalwiki/thumb/3/31/Flashlight_Icon.png/150px-Flashlight_Icon.png'),
(4,'Jetpack', 'Jetpack','This device will get you around anywhere! Just use it responsibly!',700,52,'YES','YES','https://static.miraheze.org/lethalwiki/thumb/1/1e/Jetpack_Icon.png/150px-Jetpack_Icon.png'),
(5, 'Lockpicker', 'Lockpicker','Lockpickers are tools used to gain access to locked doors',20,16,'NO','NO','https://static.miraheze.org/lethalwiki/thumb/7/75/Lockpicker_Icon.png/150px-Lockpicker_Icon.png'),
(6, 'Pro-Flashlight', 'Pro-Flashlight','With an extra battery life and even brighter bulb, your colleagues can never leave you in the dark again!',25,5,'NO','YES','https://static.miraheze.org/lethalwiki/thumb/6/6b/Pro-Flashlight_Icon.png/150px-Pro-Flashlight_Icon.png'),
(7, 'Radar_Booster', 'Radar Booster','Use the SWITCH command before the radar booster s name to view it on the main monitor. It must be activated. Use the PING command before the radar booster s name to play a special sound from the device.',60,19,'YES','NO','https://static.miraheze.org/lethalwiki/thumb/9/9c/Radar_Booster_Icon.png/150px-Radar_Booster_Icon.png'),
(8, 'Shovel', 'Shovel','For self-defense',30,8,'YES','NO','https://static.miraheze.org/lethalwiki/thumb/2/28/Shovel_Icon.png/150px-Shovel_Icon.png'),
(9, 'Spray_Paint', 'Spray Paint','pray paint is a tool item that can be used to paint walls and floors',50,0,'NO','NO','https://static.miraheze.org/lethalwiki/thumb/8/85/Spraycan_Icon.png/150px-Spraycan_Icon.png'),
(10, 'Stun_Grenade', 'Stun Grenade','Stun grenades are explosive weapons intended to disorient entities',30,5,'NO','NO','https://static.miraheze.org/lethalwiki/thumb/c/c2/Stun_Grenade_Icon.png/150px-Stun_Grenade_Icon.png'),
(11, 'TZP-Inhalant', 'TZP-Inhalant','This safe and legal medicine can be administered to see great benefits to your performance on the job',120,0,'YES','NO','https://static.miraheze.org/lethalwiki/thumb/c/cb/TZP_Icon.png/150px-TZP_Icon.png'),
(12, 'Walkie-Talkie', 'Walkie-Talkie','Useful for keeping in touch! Hear other players when the walkie talkie is in your inventory. Must be in your hand and pressed down to transmit voice',12,0,'NO','YES','https://static.miraheze.org/lethalwiki/thumb/6/6a/Walkie-Talkie_Icon.png/150px-Walkie-Talkie_Icon.png'),
(13, 'Zap_Gun', 'Zap Gun','The most specialized self-protective equipment, capable of sending upwards of 80 000 volts',400,11,'YES','YES','https://static.miraheze.org/lethalwiki/thumb/7/7b/Zap_Gun_Icon.png/150px-Zap_Gun_Icon.png');






