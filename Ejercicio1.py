import heapq

class HuffmanNode:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.symbol < other.symbol
        return self.freq < other.freq

def build_huffman_tree(symbols):
    heap = [HuffmanNode(sym, freq) for sym, freq in symbols.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(left.symbol + right.symbol, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", codebook={}):
    if node.left is None and node.right is None:
        codebook[node.symbol] = prefix
    if node.left:
        generate_codes(node.left, prefix + "0", codebook)
    if node.right:
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

def decode_huffman(encoded_message, reverse_codebook):
    decoded_message = []
    current_code = ""
    for bit in encoded_message:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_message.append(reverse_codebook[current_code])
            current_code = ""
    return ' '.join(decoded_message)

def translate_message(decoded_message, translation_dict):
    translated_message = [translation_dict.get(symbol, '') for symbol in decoded_message]
    return ' '.join(translated_message)

def verify_translation(translated_message, keywords):
    return any(keyword in translated_message for keyword in keywords)

# Diccionario inverso basado en el código de Huffman
reverse_codebook = {
    '00': 'Ankh',
    '010': 'Lotus',
    '011': 'Scarab',
    '100': 'Obelisk',
    '101': 'Djed',
    '1100': 'Sphinx',
    '1101': 'Pyramid',
    '111': 'Eye of Horus'
}

# Diccionario de traducción de jeroglíficos a significados en español
jeroglifico_a_espanol = {
    'Ankh': 'vida',
    'Lotus': 'pureza',
    'Scarab': 'transformación',
    'Obelisk': 'estabilidad',
    'Djed': 'durabilidad',
    'Sphinx': 'guardián',
    'Pyramid': 'eternidad',
    'Eye of Horus': 'protección'
}

# Mensajes codificados para decodificar
mensaje_1 = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
mensaje_2 = "0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"

# Construir el árbol de Huffman
symbols = {'Ankh': 2, 'Lotus': 3, 'Scarab': 4, 'Obelisk': 5, 'Djed': 6, 'Sphinx': 7, 'Pyramid': 8, 'Eye of Horus': 9}
huffman_tree = build_huffman_tree(symbols)

# Generar el código de Huffman
codebook = generate_codes(huffman_tree)

# Decodificación del mensaje 1
decoded_message_1 = decode_huffman(mensaje_1, reverse_codebook)

# Traducción del mensaje 1
translated_message_1 = translate_message(decoded_message_1, jeroglifico_a_espanol)

# Verificación del mensaje 1
keywords = ['vida', 'pureza', 'transformación', 'estabilidad', 'durabilidad', 'guardián', 'eternidad', 'protección']
if verify_translation(translated_message_1, keywords):
    print("Decoded Message 1:", decoded_message_1)
    print("Translated Message 1:", translated_message_1)
else:
    print("La traducción del mensaje 1 no tiene sentido.")

# Decodificación del mensaje 2
decoded_message_2 = decode_huffman(mensaje_2, reverse_codebook)

# Traducción del mensaje 2
translated_message_2 = translate_message(decoded_message_2, jeroglifico_a_espanol)

# Verificación del mensaje 2
if verify_translation(translated_message_2, keywords):
    print("Decoded Message 2:", decoded_message_2)
    print("Translated Message 2:", translated_message_2)
else:
    print("La traducción del mensaje 2 no tiene sentido.")