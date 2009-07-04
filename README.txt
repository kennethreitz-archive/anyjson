Overview
--------

Imports the best available JSON encoder and decoder from any installed json
module.

Originally part of carrot (http://github.com/ask/carrot/)

Authors
-------

Rune F. Halvorsen <runefh@gmail.com>
Ask Solem <askh@opera.com>

Changelog
---------

0.1:

 * Initial release

0.1.1

 * Added benchmarking script
 * Added support for more serializer modules

0.2

 * Added exception handling so that all supported modules will result in the
   same exceptions being thrown. The exceptions are the same that are used
   by the JSON module from python 2.7, TypeError for serialize and
   ValueError for deserialize.
 * '''NOTE''' API changed. the implementation property is now an object, not
   a string
 * Rewrote module loading code, so it's now easier to add and rearrange
   JSON modules

License
-------

This software is licensed under the ``New BSD License``:

Copyright (c) 2009, by the authors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.

Neither the name of the authors nor the names of its contributors may be used
to endorse or promote products derived from this software without specific
prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
