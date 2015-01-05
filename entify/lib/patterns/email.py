# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This file is part of entify.
#
#	entify is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################


from entify.lib.patterns.regexp import RegexpObject

class Email(RegexpObject):
	''' 
		<Email> class. It identifies emails that include:
		    foo@bar.com
		    foo[at]bar[dot]com
		    foo[arroba]bar[punto]com
		    foo [at] bar [dot] com
	'''
	def __init__(self):
		''' 
			Constructor without parameters.
			Most of the times, this will be the ONLY method needed to be overwritten.

			:param name:	string containing the name of the regular expression.
			:param reg_exp:	string containing the regular expresion.
		'''
		# This is the tag of the regexp
		self.name = "i3visio.email"
		# This is the string containing the reg_exp to be seeked
		self.reg_exp = ["([a-zA-Z0-9\.\-_]+(?:@| ?\[(?:arroba|at)\] ?)[a-zA-Z0-9\.\-]+(?:\.| ?\[(?:punto|dot)\] ?)[a-zA-Z]+)"]

		
