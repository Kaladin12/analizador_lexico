GLC = {
  "S": {
    "$": [["-"]],
    "AGR_OP": [["MAIN"], ["$"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["MAIN"], ["$"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["MAIN"], ["$"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["MAIN"], ["$"]],
    "ID": [["MAIN"], ["$"]],
    "EOL": [["-"]],
    "MNTRS": [["MAIN"], ["$"]],
    "HAZ_MNTRS": [["MAIN"], ["$"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["MAIN"], ["$"]],
    "ENTERO": [["MAIN"], ["$"]],
    "FLOTANTE": [["MAIN"], ["$"]],
    "SIONO": [["MAIN"], ["$"]],
    "VAL_CAD": [["MAIN"], ["$"]],
    "VAL_SIONO": [["MAIN"], ["$"]],
    "VAL_ENT": [["MAIN"], ["$"]],
    "VAL_FLOT": [["MAIN"], ["$"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["MAIN"], ["$"]],
    "IMPR": [["MAIN"], ["$"]],
    "LONGITUD": [["MAIN"], ["$"]]
  },
  "MAIN": {
    "$": [["-"]],
    "AGR_OP": [["EXPR"], ['MORE']],
    "AGR_CP": [["-"]],
    "COND_IF": [["ESTRUCT"],['MORE']],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["ESTRUCT"], ['MORE']],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["ESTRUCT"], ['MORE']],
    "ID": [["EXPR"], ['MORE']],
    "EOL": [["-"]],
    "MNTRS": [["ESTRUCT"], ['MORE']],
    "HAZ_MNTRS": [["ESTRUCT"], ['MORE']],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["ASIGN"], ['MORE']],
    "ENTERO": [["ASIGN"], ['MORE']],
    "FLOTANTE": [["ASIGN"], ['MORE']],
    "SIONO": [["ASIGN"], ['MORE']],
    "VAL_CAD": [["EXPR"], ['MORE']],
    "VAL_SIONO": [["EXPR"], ['MORE']],
    "VAL_ENT": [["EXPR"], ['MORE']],
    "VAL_FLOT": [["EXPR"], ['MORE']],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["ESTRUCT"], ['MORE']],
    "IMPR": [["ESTRUCT"], ['MORE']],
    "LONGITUD": [["ESTRUCT"], ['MORE']]
  },
  "EXPR": {
    "$": [["-"]],
    "AGR_OP": [["AGR_OP"], ["EXPR"], ["AGR_CP"], ["V"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["VALOR"], ["V"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["VALOR"], ["V"]],
    "VAL_SIONO": [["VALOR"], ["V"]],
    "VAL_ENT": [["VALOR"], ["V"]],
    "VAL_FLOT": [["VALOR"], ["V"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "V": {
    "$": [[""]],
    "AGR_OP": [["-"]],
    "AGR_CP": [[""]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [[""]],
    "AGR_CB": [[""]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [[""]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [[""]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["ARI_PS"], ["EXPR"]],
    "ARI_SUBS": [["ARI_PS"], ["EXPR"]],
    "ARI_MULT": [["ARI_MD"], ["T"], ["X"]],
    "ARI_DIV": [["ARI_MD"], ["T"], ["X"]],
    "OP_IGIG": [["OPREL"], ["EXPR"]],
    "OP_MAY": [["OPREL"], ["EXPR"]],
    "OP_MEN": [["OPREL"], ["EXPR"]],
    "OP_MAI": [["OPREL"], ["EXPR"]],
    "OP_MEI": [["OPREL"], ["EXPR"]],
    "OP_DIF": [["OPREL"], ["EXPR"]],
    "AND": [["OPLOG"], ["T"], ["X"]],
    "OR": [["OPLOG"], ["T"], ["X"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "X": {
    "$": [[""]],
    "AGR_OP": [["-"]],
    "AGR_CP": [[""]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [[""]],
    "AGR_CB": [[""]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [[""]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [[""]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["ARI_PS"], ["EXPR"]],
    "ARI_SUBS": [["ARI_PS"], ["EXPR"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["OPREL"], ["EXPR"]],
    "OP_MAY": [["OPREL"], ["EXPR"]],
    "OP_MEN": [["OPREL"], ["EXPR"]],
    "OP_MAI": [["OPREL"], ["EXPR"]],
    "OP_MEI": [["OPREL"], ["EXPR"]],
    "OP_DIF": [["OPREL"], ["EXPR"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "T": {
    "$": [["-"]],
    "AGR_OP": [["AGR_OP"], ["EXPR"], ["AGR_CP"], ["U"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["VALOR"], ["U"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["VALOR"], ["U"]],
    "VAL_SIONO": [["VALOR"], ["U"]],
    "VAL_ENT": [["VALOR"], ["U"]],
    "VAL_FLOT": [["VALOR"], ["U"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "U": {
    "$": [[""]],
    "AGR_OP": [["-"]],
    "AGR_CP": [[""]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [[""]],
    "AGR_CB": [[""]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [[""]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [[""]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [[""]],
    "ARI_SUBS": [[""]],
    "ARI_MULT": [["ARI_MD"], ["T"]],
    "ARI_DIV": [["ARI_MD"], ["T"]],
    "OP_IGIG": [[""]],
    "OP_MAY": [[""]],
    "OP_MEN": [[""]],
    "OP_MAI": [[""]],
    "OP_MEI": [[""]],
    "OP_DIF": [[""]],
    "AND": [["OPLOG"], ["T"]],
    "OR": [["OPLOG"], ["T"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "ESTRUCT": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["COND"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["INTER"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["LOOP"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["LOOP"]],
    "HAZ_MNTRS": [["LOOP"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["LLAMA_AUX"]],
    "IMPR": [["LLAMA_AUX"]],
    "LONGITUD": [["LLAMA_AUX"]]
  },
  "COND": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["COND_IF"], ["IF_CONTENT"], ["TEMP"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "TEMP": {
    "$": [[""]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["COND_ELSE"], ["CONTENT"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [[""]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [[""]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "IF_CONTENT": {
    "$": [["-"]],
    "AGR_OP": [["AGR_OP"], ["EXPR"], ["AGR_CP"], ["CONTENT"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "CONTENT": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["AGR_OB"], ["MAIN"], ["AGR_CB"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "INTER": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [
      ["INTERRUPTOR"],
      ["AGR_OP"],
      ["EXPR"],
      ["AGR_CP"],
      ["AGR_OB"],
      ["CASE_"],
      ["AGR_CB"]
    ],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "CASE_": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [
      ["CASO"],
      ["AGR_OP"],
      ["VALOR"],
      ["AGR_CP"],
      ["AGR_OB"],
      ["MAIN"],
      ["ROMPER"],
      ["AGR_CB"],
      ["CASE_END"]
    ],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "CASE_END": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["CASE_"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["DEFAULT"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "DEFAULT": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [
      ["PREDETERMINADO"],
      ["AGR_OB"],
      ["MAIN"],
      ["ROMPER"],
      ["AGR_CB"]
    ],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "LOOP": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["LOOP_FOR_ABS"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["LOOP_WHILE"]],
    "HAZ_MNTRS": [["LOOP_DO"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "LOOP_FOR_ABS": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["CADA"], ["AGR_OP"], ["FORS"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "FORS": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["LOOP_PY"], ["ID"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["LOOP_FOR"]],
    "ENTERO": [["LOOP_FOR"]],
    "FLOTANTE": [["LOOP_FOR"]],
    "SIONO": [["LOOP_FOR"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "LOOP_FOR": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [
      ["ASIGN"],
      ["EOL"],
      ["EXPR"],
      ["EOL"],
      ["EXPR"],
      ["AGR_CP"],
      ["CONTENT"]
    ],
    "ENTERO": [
      ["ASIGN"],
      ["EOL"],
      ["EXPR"],
      ["EOL"],
      ["EXPR"],
      ["AGR_CP"],
      ["CONTENT"]
    ],
    "FLOTANTE": [
      ["ASIGN"],
      ["EOL"],
      ["EXPR"],
      ["EOL"],
      ["EXPR"],
      ["AGR_CP"],
      ["CONTENT"]
    ],
    "SIONO": [
      ["ASIGN"],
      ["EOL"],
      ["EXPR"],
      ["EOL"],
      ["EXPR"],
      ["AGR_CP"],
      ["CONTENT"]
    ],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "LOOP_WHILE": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["MNTRS"], ["AGR_OP"], ["EXPR"], ["CONTENT"], ["EOL"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "LOOP_DO": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["HAZ_MNTRS"], ["CONTENT"], ["EXPR"], ["EOL"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "LOOP_PY": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [
      ["EN"],
      ["RANGO"],
      ["AGR_OP"],
      ["EXPR"],
      ["AGR_CP"],
      ["AGR_CP"],
      ["CONTENT"]
    ],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "ASIGN": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["TIPO"], ["ID"], ["OP_ASIG"], ["EXPR"], ["EOL"]],
    "ENTERO": [["TIPO"], ["ID"], ["OP_ASIG"], ["EXPR"], ["EOL"]],
    "FLOTANTE": [["TIPO"], ["ID"], ["OP_ASIG"], ["EXPR"], ["EOL"]],
    "SIONO": [["TIPO"], ["ID"], ["OP_ASIG"], ["EXPR"], ["EOL"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "TIPO": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["CADENA"]],
    "ENTERO": [["ENTERO"]],
    "FLOTANTE": [["FLOTANTE"]],
    "SIONO": [["SIONO"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "VALOR": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["ID"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["VAL_CAD"]],
    "VAL_SIONO": [["VAL_SIONO"]],
    "VAL_ENT": [["VAL_ENT"]],
    "VAL_FLOT": [["VAL_FLOT"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "ARI_PS": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["ARI_PLUS"]],
    "ARI_SUBS": [["ARI_SUBS"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "ARI_MD": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["ARI_MULT"]],
    "ARI_DIV": [["ARI_DIV"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "OPREL": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["OP_IGIG"]],
    "OP_MAY": [["OP_MAY"]],
    "OP_MEN": [["OP_MEN"]],
    "OP_MAI": [["OP_MAI"]],
    "OP_MEI": [["OP_MEI"]],
    "OP_DIF": [["OP_DIF"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "OPLOG": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["AND"]],
    "OR": [["OR"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "LLAMA_AUX": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["SLEEP"]],
    "IMPR": [["PRINT"]],
    "LONGITUD": [["LEN"]]
  },
  "SLEEP": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["SLP"], ["AGR_OP"], ["VALOR"], ["AGR_CP"]],
    "IMPR": [["-"]],
    "LONGITUD": [["-"]]
  },
  "PRINT": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["IMPR"], ["AGR_OP"], ["EXPR"], ["AGR_CP"]],
    "LONGITUD": [["-"]]
  },
  "LEN": {
    "$": [["-"]],
    "AGR_OP": [["-"]],
    "AGR_CP": [["-"]],
    "COND_IF": [["-"]],
    "COND_ELSE": [["-"]],
    "AGR_OB": [["-"]],
    "AGR_CB": [["-"]],
    "INTERRUPTOR": [["-"]],
    "CASO": [["-"]],
    "ROMPER": [["-"]],
    "PREDETERMINADO": [["-"]],
    "CADA": [["-"]],
    "ID": [["-"]],
    "EOL": [["-"]],
    "MNTRS": [["-"]],
    "HAZ_MNTRS": [["-"]],
    "EN": [["-"]],
    "RANGO": [["-"]],
    "OP_ASIG": [["-"]],
    "CADENA": [["-"]],
    "ENTERO": [["-"]],
    "FLOTANTE": [["-"]],
    "SIONO": [["-"]],
    "VAL_CAD": [["-"]],
    "VAL_SIONO": [["-"]],
    "VAL_ENT": [["-"]],
    "VAL_FLOT": [["-"]],
    "ARI_PLUS": [["-"]],
    "ARI_SUBS": [["-"]],
    "ARI_MULT": [["-"]],
    "ARI_DIV": [["-"]],
    "OP_IGIG": [["-"]],
    "OP_MAY": [["-"]],
    "OP_MEN": [["-"]],
    "OP_MAI": [["-"]],
    "OP_MEI": [["-"]],
    "OP_DIF": [["-"]],
    "AND": [["-"]],
    "OR": [["-"]],
    "SLP": [["-"]],
    "IMPR": [["-"]],
    "LONGITUD": [["LONGITUD"], ["AGR_OP"], ["VALOR"], ["AGR_CP"]]
  },
  'MORE' :{
    "$": [[""]],
    "AGR_OP": [["MAIN"]],
    "AGR_CP": [[""]],
    "COND_IF": [["MAIN"]],
    "COND_ELSE": [[""]],
    "AGR_OB": [[""]],
    "AGR_CB": [[""]],
    "INTERRUPTOR": [["MAIN"]],
    "CASO": [[""]],
    "ROMPER": [[""]],
    "PREDETERMINADO": [[""]],
    "CADA": [["MAIN"]],
    "ID": [["MAIN"]],
    "EOL": [[""]],
    "MNTRS": [["MAIN"]],
    "HAZ_MNTRS": [["MAIN"]],
    "EN": [[""]],
    "RANGO": [[""]],
    "OP_ASIG": [[""]],
    "CADENA": [["MAIN"]],
    "ENTERO": [["MAIN"]],
    "FLOTANTE": [["MAIN"]],
    "SIONO": [["MAIN"]],
    "VAL_CAD": [["MAIN"]],
    "VAL_SIONO": [["MAIN"]],
    "VAL_ENT": [["MAIN"]],
    "VAL_FLOT": [["MAIN"]],
    "ARI_PLUS": [[""]],
    "ARI_SUBS": [[""]],
    "ARI_MULT": [[""]],
    "ARI_DIV": [[""]],
    "OP_IGIG": [[""]],
    "OP_MAY": [[""]],
    "OP_MEN": [[""]],
    "OP_MAI": [[""]],
    "OP_MEI": [[""]],
    "OP_DIF": [[""]],
    "AND": [[""]],
    "OR": [[""]],
    "SLP": [["MAIN"]],
    "IMPR": [["MAIN"]],
    "LONGITUD": [['MAIN']]
  }
}
