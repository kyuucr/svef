#!/usr/bin/env python

#
#  Copyright 2009 Claudio Pisa (claudio dot pisa at uniroma2 dot it)
#
#  This file is part of SVEF (SVC Streaming Evaluation Framework).
#
#  SVEF is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  SVEF is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with SVEF.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
from nalulib import *

if len(sys.argv) < 3:
	print "Usage: %s <original stream's trace> <level to purge>" % sys.argv[0]
	sys.exit(1)

originaltraceptfilename = sys.argv[1]
level2purge = int(sys.argv[2])

print "Start-Pos.  Length  LId  TId  QId   Packet-Type  Discardable  Truncatable"
print "==========  ======  ===  ===  ===  ============  ===========  ==========="

# load lines from the original trace file
originaltracefile = open(originaltraceptfilename)
for line in originaltracefile:
		try:
				nalu = NALU(line)
				if nalu.lid >= 0 and nalu.lid != level2purge:
						print nalu
		except NALUException:
				pass
originaltracefile.close()



