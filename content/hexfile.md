Title: Parsing Intel Hex Files with Python
Date: 2014-09-25 8:39 PM

One of my recent projects called for the parsing of [Intel Hex](http://en.wikipedia.org/wiki/Intel_HEX) files to extract certain bits of static information from some precompiled microcontroller code.  Intel Hex is a well documented file format standard, but it's not something that parses itself, particularly if you don't deal with it very frequently (as I don't)

I wrote a python module to deal with this, which wraps up the parsing of the hex file itself.  I found another module to do this: [IntelHex](https://pypi.python.org/pypi/IntelHex/1.1) but had difficulty with installing it.  From a look at the documentation, though, it seems that the IntelHex package was designed for the same purpose I had:  To sift through hex files for Microchip's PIC16 series microcontrollers.

The API is simple.  Matters are complicated slightly by the fact that the Intel hex file format allows for multiple discontinuous memory segments to be defined.  You're not just reading a single block of binary data, but a collection of one or more distinct binary segments:

	:::python
	import hexfile

	f = hexfile.load('memory.hex')

	print f.segments

The above example prints all the segments in the file.  Indexing hex file object acts like a byte index into its memory contents.  Given the address provided, the hex file object chooses the correct segment from which to retrieve the data:

	:::python

	f = hexfile.load('memory.hex')
	
	# Print the bytes in addresses 16-31 in the file
	for i in range(16,32):
		print f[i]

You can also address segments individually.  The code below is equivalent to the code above (assuming the first segment in the file starts at address 0x00):

	:::python

	f = hexfile.load('memory.hex')

	# Print the bytes in addresses 16-31 in the file
	for i in range(16,32):
		print f.segments[0][i]

I'm not sure how I feel about the segment addressing.  Each segment has a `start_address` member that indicates the segment start.  I have considered making segment indexing segment local, so that when you index into a segment, you're not using the absolute memory address, but the address relative to the start of the segment.  If for instance the segment in the example above started at address 16 instead of 0 and we were using segment-local addressing the example above would look like this instead:

	:::python
	# Print the bytes in addresses 16-31 in the file
	for i in range(16):
		print f.segments[0][i]

We're asking for bytes 0-15 of the segment, but since the segment base address is 16, that gives us bytes 16-31.  I'm still on the fence.  Another issue is iteration.   Iteration over a segment is easy:

	:::python
	for byte in f.segments[0]:
		print "0x%02x" % byte

The above example gives me every byte of segment 0 of the file.  I can do a similar move over the whole file:

	:::python
	for byte in f:
		print "0x02x" % byte

This gives me every byte in the file, but of course for an entire Intel hex file, it's likely that those bytes are non-contiguous at segment boundaries.  Is it weird to be able to iterate over an address space that's non contiguous?  It might make more sense to provide something more like python's [enumerate()](https://docs.python.org/2/library/functions.html#enumerate) function, where both the address and data are returned at each iteration. In this case, though, I'm wondering how useful it is to iterate over the entire file at all - you'd probably be dealing one segment at a time, so this iteration tactic wouldn't be often used.

In any case, my hexfile module can be installed easily with pip (`pip install hexfile`) and you can take it for a spin yourself.  The files are up on [Github](https://github.com/ryansturmer/hexfile)