# Experiments with a custom ARINC 429 protocol
#
#


class A429_word:
    # Generic A429 Word

    def __init__(self, label, encoding, sdi, ssm, data) -> None:
        self.label = label
        self.encoding = encoding
        self.sdi = sdi
        self.ssm = ssm
        self.data = data
            
    def __str__(self):
        return f"L: {self.label} \nE: {self.encoding} \nSDI: {self.sdi} \nSSM: {self.ssm} \nData: {self.data}"

    # Encode A429 word as BNR, returning a properly formatted byte array for TX
    def encode_A429_BNR(self, a429_real):
        pass

    # Decode BNR A429 word byte array after RX, returning a complete word
    def decode_A429_BNR(self, a429_bnr):
        pass

    
