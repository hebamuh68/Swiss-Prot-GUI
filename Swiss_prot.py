import streamlit as st


class Swiss_prot:

    def __init__(self, filepath):
        self.file = filepath
        self.hash_file = {}
        self.rf_hash_file = {}
        self.sq_hash_file = {}

        for i in self.file:
            each_line = i.split("   ")
            each_line_id = each_line[0]

            # SQ case:
            if each_line_id == "":
                each_line_id = "SQ"

            # Reference case
            if each_line_id in ['RN', 'RP', 'RC', 'RX', 'RA', 'RL', 'RT']:
                if each_line_id == "RN":
                    ref_number = f"Refernce {each_line[1].strip()}: "
                    if ref_number not in self.rf_hash_file:
                        self.rf_hash_file[ref_number] = {}
                else:
                    if each_line_id not in self.rf_hash_file[ref_number]:
                        self.rf_hash_file[ref_number][each_line_id] = ["   ".join(each_line[1:]).strip()]
                    else:
                        self.rf_hash_file[ref_number][each_line_id] += ["   ".join(each_line[1:]).strip()]

            # FT case
            elif each_line_id == "FT":
                if each_line_id not in self.hash_file:
                    self.hash_file[each_line_id] = [each_line[1:]]
                else:
                    self.hash_file[each_line_id] += [each_line[1:]]

            # Other cases
            elif each_line_id not in self.hash_file:
                self.hash_file[each_line_id] = ["   ".join(each_line[1:]).strip()]
            else:
                self.hash_file[each_line_id] += ["  ".join(each_line[1:]).strip()]

    # ID - Identification.
    def get_ID(self):
        if 'ID' not in self.hash_file: return "This record doesn't exist in this file"
        return self.hash_file["ID"][0]

    # AC - Accession number(s).
    def get_AC(self):
        if 'AC' not in self.hash_file: return "This record doesn't exist in this file"
        return "\n ".join(self.hash_file["AC"])

    # DT - Date.
    def get_DT(self):
        if 'DT' not in self.hash_file: return "This record doesn't exist in this file"
        return "\n".join(self.hash_file["DT"])

    # DE - Description.
    def get_DE(self):
        if 'DE' not in self.hash_file: return "This record doesn't exist in this file"
        # return "\n".join(self.hash_file["DE"])
        return [i for i in self.hash_file["DE"]]

    # GN - Gene name(s).
    def get_GN(self):
        if 'GN' not in self.hash_file: return "This record doesn't exist in this file"
        return "\n".join(self.hash_file["GN"])

    # OS - Organism species.
    def get_OS(self):
        if 'OS' not in self.hash_file: return "This record doesn't exist in this file"
        return "\n".join(self.hash_file["OS"])

    # OG - Organelle.
    def get_OG(self):
        if 'OG' not in self.hash_file: return "This record doesn't exist in this file"
        return self.hash_file["OG"]

    # OC - Organism classification.
    def get_OC(self):
        if 'OC' not in self.hash_file: return "This record doesn't exist in this file"
        return " ".join(self.hash_file["OC"])

    # RN - Reference info.
    def get_RN(self):
        # if 'RN' not in self.hash_file: return "This record doesn't exist in this file"
        return self.rf_hash_file

    # CC - Comments or notes.
    def get_CC(self):
        if 'CC' not in self.hash_file: return "This record doesn't exist in this file"
        CC_content = []
        note = ""
        for i in self.hash_file["CC"]:
            if i[0:3] == "-!-":
                note += "\n"
                note += i
            else:
                note += i
                note += "   \n  "
                CC_content.append(note)
                note = ""
        return "    ".join(CC_content)

    # DR - Database cross-references.
    def get_DR(self):
        if 'DR' not in self.hash_file: return "This record doesn't exist in this file"
        o = ""
        for i in self.hash_file["DR"]:
            o += str(i)
            o += "\n\n"
        return o

    # KW - Keywords.
    def get_KW(self):
        if 'KW' not in self.hash_file: return "This record doesn't exist in this file"
        return "".join(self.hash_file["KW"])

    # FT - Feature table data.
    def get_FT(self):
        if 'FT' not in self.hash_file: return "This record doesn't exist in this file"
        o = ""
        for i in self.hash_file["FT"]:
            o += str("  ".join(i))
            o += "\n"
        return o

    # SQ - Sequence header & data.
    def get_SQ(self):
        if 'SQ' not in self.hash_file: return "This record doesn't exist in this file"
        header = self.hash_file["SQ"][0]
        sequence = "".join(self.hash_file["SQ"][1:])
        return (f"Header: {header},\n\n Sequence: \n\n {sequence}")


obj = Swiss_prot('swiss_prot')
print(obj.get_CC())


# CC - Comments or notes.
def get_CC(self):
    if 'CC' not in self.hash_file: return "This record doesn't exist in this file"
    return "\n".join(self.hash_file["CC"])
