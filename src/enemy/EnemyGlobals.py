from panda3d.core import VBase4
from . import EnemyDNA

SCALE_INDEX = 0 # The scale of the cog
HAND_COLOR_INDEX = 1 # The hand color
HEADS_INDEX = 2 # A list of heads
HEAD_TEXTURE_INDEX = 3 # The texture to use for the head
HEIGHT_INDEX = 4 # The height of the cog

aSize = 6.06 # Size of body type 'a'
bSize = 5.29 # Size of body type 'b'
cSize = 4.14 # Size of body type 'c'

ColdCallerHead = VBase4(0.25, 0.35, 1.0, 1.0) # Head used by Cold Caller

enemyProperties = {# Bossbots
                  'f': (4.0 / cSize, EnemyDNA.corpPolyColor, ['flunky', 'glasses'], '', 4.88),
                  'p': (3.35 / bSize, EnemyDNA.corpPolyColor, ['pencilpusher'], '', 5.0),
                  'ym': (4.125 / aSize, EnemyDNA.corpPolyColor, ['yesman'], '', 5.28),
                  'mm': (2.5 / cSize, EnemyDNA.corpPolyColor, ['micromanager'], '', 3.25),
                  'ds': (4.5 / bSize, EnemyDNA.corpPolyColor, ['beancounter'], '', 6.08),
                  'hh': (6.5 / aSize, EnemyDNA.corpPolyColor, ['headhunter'], '', 7.45),
                  'cr': (6.75 / cSize, VBase4(0.85, 0.55, 0.55, 1.0), ['flunky'], 'corporate-raider.jpg', 8.23),
                  'tbc': (7.0 / aSize, VBase4(0.75, 0.95, 0.75, 1.0), ['bigcheese'], '', 9.34),
                  # Lawbots
                  'bf': (4.0 / cSize, EnemyDNA.legalPolyColor, ['tightwad'], 'bottom-feeder.jpg', 4.81),
                  'b': (4.375 / bSize, VBase4(0.95, 0.95, 1.0, 1.0), ['movershaker'], 'blood-sucker.jpg', 6.17),
                  'dt': (4.25 / aSize, EnemyDNA.legalPolyColor, ['twoface'], 'double-talker.jpg', 5.63),
                  'ac': (4.35 / bSize, EnemyDNA.legalPolyColor, ['ambulancechaser'], '', 6.39),
                  'bs': (4.5 / aSize, EnemyDNA.legalPolyColor, ['backstabber'], '', 6.71),
                  'sd': (5.65 / bSize, VBase4(0.5, 0.8, 0.75, 1.0), ['telemarketer'], 'spin-doctor.jpg', 7.9),
                  'le': (7.125 / aSize, VBase4(0.25, 0.25, 0.5, 1.0), ['legaleagle'], '', 8.27),
                  'bw': (7.0 / aSize, EnemyDNA.legalPolyColor, ['bigwig'], '', 8.69),
                  # Cashbots
                  'sc': (3.6 / cSize, EnemyDNA.moneyPolyColor, ['coldcaller'], '', 4.77),
                  'pp': (3.55 / aSize, VBase4(1.0, 0.5, 0.6, 1.0), ['pennypincher'], '', 5.26),
                  'tw': (4.5 / cSize, EnemyDNA.moneyPolyColor, ['tightwad'], '', 5.41),
                  'bc': (4.4 / bSize, EnemyDNA.moneyPolyColor, ['beancounter'], '', 5.95),
                  'nc': (5.25 / aSize, EnemyDNA.moneyPolyColor, ['numbercruncher'], '', 7.22),
                  'mb': (5.3 / cSize, EnemyDNA.moneyPolyColor, ['moneybags'], '', 6.97),
                  'ls': (6.5 / bSize, VBase4(0.5, 0.85, 0.75, 1.0), ['loanshark'], '', 8.58),
                  'rb': (7.0 / aSize, EnemyDNA.moneyPolyColor, ['yesman'], 'robber-baron.jpg', 8.95),
                  # Sellbots
                  'cc': (3.5 / cSize, VBase4(0.55, 0.65, 1.0, 1.0), ['coldcaller'], '', 4.63),
                  'tm': (3.75 / bSize, EnemyDNA.salesPolyColor, ['telemarketer'], '', 5.24),
                  'nd': (4.35 / aSize, EnemyDNA.salesPolyColor, ['numbercruncher'], 'name-dropper.jpg', 5.98),
                  'gh': (4.75 / cSize, EnemyDNA.salesPolyColor, ['gladhander'], '', 6.4),
                  'ms': (4.75 / bSize, EnemyDNA.salesPolyColor, ['movershaker'], '', 6.7),
                  'tf': (5.25 / aSize, EnemyDNA.salesPolyColor, ['twoface'], '', 6.95),
                  'm': (5.75 / aSize, EnemyDNA.salesPolyColor, ['twoface'], 'mingler.jpg', 7.61),
                  'mh': (7.0 / aSize, EnemyDNA.salesPolyColor, ['yesman'], '', 8.95)
}