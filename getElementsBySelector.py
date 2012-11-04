#Get DOM elements based on the given CSS Selector - V 1.00.A Beta
#Direct port of http://www.openjs.com/scripts/dom/css_selector/
def getElementsBySelector(all_selectors, document):
	selected = []
	import re, string
	
	all_selectors = re.sub(r'\s*([^\w])\s*',r'\1', all_selectors) #Remove the 'beautification' spaces
	
	# Grab all of the tagName elements within current context	
	def getElements(context,tag):
		if (tag == ""): tag = '*'
		
		# Get elements matching tag, filter them for class selector
		found = []
		for con in context:
			eles = con.getElementsByTagName(tag)
			found.extend(eles)
		
		return found

	context = [document]
	inheriters = string.split(all_selectors, " ")

	# Space
	for element in inheriters:
		#This part is to make sure that it is not part of a CSS3 Selector
		left_bracket = string.find(element,"[")
		right_bracket = string.find(element,"]")
		pos = string.find(element,"#") #ID
		
		if(pos+1 and not(pos>left_bracket and pos<right_bracket)):
			parts = string.split(element, "#")
			tag = parts[0]
			id = parts[1]
			ele = document.getElementById(id)
			
			context = [](ele)
			continue
		

		pos = string.find(element,".")#Class
		if(pos+1 and not(pos>left_bracket and pos<right_bracket)):
			parts = string.split(element, '.')
			tag = parts[0]
			class_name = parts[1]

			found = getElements(context, tag)
			context = []
			for fnd in found:
				if(fnd.getAttribute("class") and re.search(r'(^|\s)'+class_name+'(\s|$)', fnd.getAttribute("class"))): context.append(fnd)
			
			continue
		

		if(string.find(element,'[')+1):#If the char '[' appears, that means it needs CSS 3 parsing
			# Code to deal with attribute selectors
			m = re.match(r'^(\w*)\[(\w+)([=~\|\^\$\*]?)=?[\'"]?([^\]\'"]*)[\'"]?\]$', element)
			if (m):
				tag = m.group(1)
				attr = m.group(2)
				operator = m.group(3)
				value = m.group(4)
			
			found = getElements(context,tag)
			context = []
			for fnd in found:
				if(operator=='=' and fnd.getAttribute(attr) != value): continue
				if(operator=='~' and not(re.search(r'(^|\\s)'+value+'(\\s|$)',  fnd.getAttribute(attr)))): continue
				if(operator=='|' and not(re.search(r'^'+value+'-?', fnd.getAttribute(attr)))): continue
				if(operator=='^' and string.find(fnd.getAttribute(attr), value)!=0): continue
				if(operator=='$' and string.rfind(fnd.getAttribute(attr), value) != (fnd.getAttribute(attr).length-value.length)): continue
				if(operator=='*' and not(string.find(fnd.getAttribute(attr), value)+1)): continue
				
				elif(not fnd.getAttribute(attr)): continue
				context.append(fnd)

			continue
		
		#Tag selectors - no class or id specified.
		found = getElements(context,element)
		context = found
	
	selected.extend(context)
	return selected
