## sha1 calculation

SHA-1 (Secure Hash Algorithm 1) creates a 160-bit hash value from an input. Here's a simple breakdown:

1. **Pre-processing**:
   - **Padding**: The input is padded so its length is a multiple of 512 bits. Padding involves adding a '1' bit, followed by '0' bits, and finally the original message length in bits.
   - **Parsing**: The padded message is divided into 512-bit blocks.

2. **Hash Computation**:
   - Initialize five 32-bit words, \(H_0\) to \(H_4\), with specific hexadecimal values.
   - For each 512-bit block:
     - Break block into sixteen 32-bit words \(W_0\) to \(W_{15}\).
     - Extend these to eighty 32-bit words.
     - Initialize a 160-bit buffer (A, B, C, D, E) with \(H_0\) to \(H_4\).
     - Main loop: Uses a function that varies per 20 rounds, operating on the buffer and words.
     - Add the compressed chunk to the current hash value.

3. **Output**:
   - After processing all blocks, the output is a 160-bit (20-byte) hash value.

Let's hash "Hello" as an example.

The SHA-1 hash of "Hello" is `f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0`. This is a 160-bit representation of the input.

## What are the five 32 bit words?

The five 32-bit words in SHA-1 are initialization constants used at the start of the hashing process. These constants are part of the SHA-1 algorithm's design. Here they are:

1. **H0**: `0x67452301`
2. **H1**: `0xEFCDAB89`
3. **H2**: `0x98BADCFE`
4. **H3**: `0x10325476`
4. **H4**: `0xC3D2E1F0`

Each is a 32-bit value (8 hexadecimal digits). During the hashing process, these constants are used as initial values for the variables (A, B, C, D, E) which are processed and manipulated with each 512-bit block of the input data. This manipulation involves bitwise operations, modular additions, and functions specific to different rounds of the algorithm.

Those five 32-bit words in SHA-1 never change, regardless of the input. They are fixed initial values defined by the SHA-1 algorithm. The magic of SHA-1 (and other hashing algorithms) lies in how it processes the input data and manipulates these initial values in a complex way, leading to a unique hash for different inputs. But the starting point, these five constants, remains the same for every computation.

## padding example

Let's go through an example of padding in SHA-1. The process adds bits to the end of your message so its length is a multiple of 512 bits. Here's how it works:

1. **Append a single '1' bit** to the end of your message.
2. **Append '0' bits** until the message length is 64 bits less than a multiple of 512.
3. **Append the original message length** (in bits) as a 64-bit big-endian integer.

For a simple example, let's use the message "Hi" (which is 16 bits long in ASCII).

1. "Hi" in binary (ASCII) is `01001000 01101001`.

2. First, add '1': `01001000 01101001 1`.

3. Now, pad with zeros. We need the total length to be 448 bits (512 - 64), so we add 430 zeros (448 - 16 - 1).

4. Finally, add the original length in binary, which is `00000000 00000000 00000000 00000000 00000000 00000000 00000000 00010000` (16 in 64-bit big-endian format).

5. The final padded message will be quite long, so I'll calculate and show you the first and last few bits to illustrate.

   Here's the padded message for "Hi":

   - Beginning: `0100100001101001` followed by many zeros.
   - Ending: `...00000000000010000` (this represents the original length, 16 bits, in 64-bit format).

   The middle part, which I've omitted, is just a long string of zeros. This process ensures that the final message length is a multiple of 512 bits, ready for SHA-1 processing. 

## parsing

After the padding step in SHA-1, the message undergoes parsing. Here's what happens:

1. **Divide into 512-bit Blocks**: The padded message is divided into blocks, each 512 bits long. This is because SHA-1 processes the message in chunks of this size.

2. **Process Each Block**: Each of these 512-bit blocks is then processed one at a time through a series of complex operations. This is where the hash starts to take shape.

For example, if your padded message is 1024 bits long after padding, it will be split into two 512-bit blocks. If it's exactly 512 bits long, it will be just one block. The SHA-1 algorithm then processes each block through its compression function, which involves the five initial constants and a series of bitwise operations, additions, and logical functions. This is how the algorithm ensures that even a small change in the input message leads to a significantly different hash.