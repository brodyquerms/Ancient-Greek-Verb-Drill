import random
import streamlit as st


# ============================================================
# BASIC LABELS
# ============================================================

PERSONS = [
    "1st singular",
    "2nd singular",
    "3rd singular",
    "1st plural",
    "2nd plural",
    "3rd plural",
]

FORM_TYPES = [
    "Indicative",
    "Infinitive",
    "Imperative",
    "Participle",
]


# ============================================================
# VERB DATA
#
# Each paradigm contains:
#
# "indicative"  -> six finite forms
# "infinitive"  -> one infinitive, if applicable
# "imperative"  -> 2nd sg and 2nd pl, if applicable
# "participle"  -> nominative singular m/f/n, if applicable
#
# ============================================================

VERBS = {

        # ========================================================
    # τίθημι
    # ========================================================

    "τίθημι": {

        ("present", "active"): {
            "indicative": [
                "τίθημι",
                "τίθης",
                "τίθησι(ν)",
                "τίθεμεν",
                "τίθετε",
                "τιθέασι(ν)",
            ],
            "infinitive": "τιθέναι",
            "imperative": {
                "2nd singular": "τίθει",
                "2nd plural": "τίθετε",
            },
            "participle": {
                "masculine": "τιθείς",
                "feminine": "τιθεῖσα",
                "neuter": "τιθέν",
            },
        },

        ("present", "middle/passive"): {
            "indicative": [
                "τίθεμαι",
                "τίθεσαι",
                "τίθεται",
                "τιθέμεθα",
                "τίθεσθε",
                "τίθενται",
            ],
            "infinitive": "τίθεσθαι",
            "imperative": {
                "2nd singular": "τίθεσο",
                "2nd plural": "τίθεσθε",
            },
            "participle": {
                "masculine": "τιθέμενος",
                "feminine": "τιθεμένη",
                "neuter": "τιθέμενον",
            },
        },

        ("imperfect", "active"): {
            "indicative": [
                "ἐτίθην",
                "ἐτίθεις",
                "ἐτίθει",
                "ἐτίθεμεν",
                "ἐτίθετε",
                "ἐτίθεσαν",
            ],
        },

        ("imperfect", "middle/passive"): {
            "indicative": [
                "ἐτιθέμην",
                "ἐτίθεσο",
                "ἐτίθετο",
                "ἐτιθέμεθα",
                "ἐτίθεσθε",
                "ἐτίθεντο",
            ],
        },

        ("future", "active"): {
            "indicative": [
                "θήσω",
                "θήσεις",
                "θήσει",
                "θήσομεν",
                "θήσετε",
                "θήσουσι(ν)",
            ],
            "infinitive": "θήσειν",
            "participle": {
                "masculine": "θήσων",
                "feminine": "θήσουσα",
                "neuter": "θῆσον",
            },
        },

        ("future", "middle"): {
            "indicative": [
                "θήσομαι",
                "θήσῃ",
                "θήσεται",
                "θησόμεθα",
                "θήσεσθε",
                "θήσονται",
            ],
            "infinitive": "θήσεσθαι",
            "participle": {
                "masculine": "θησόμενος",
                "feminine": "θησομένη",
                "neuter": "θησόμενον",
            },
        },

        ("future", "passive"): {
            "indicative": [
                "τεθήσομαι",
                "τεθήσῃ",
                "τεθήσεται",
                "τεθησόμεθα",
                "τεθήσεσθε",
                "τεθήσονται",
            ],
            "infinitive": "τεθήσεσθαι",
            "participle": {
                "masculine": "τεθησόμενος",
                "feminine": "τεθησομένη",
                "neuter": "τεθησόμενον",
            },
        },

        ("aorist", "active"): {
            "indicative": [
                "ἔθηκα",
                "ἔθηκας",
                "ἔθηκε(ν)",
                "ἔθεμεν",
                "ἔθετε",
                "ἔθεσαν",
            ],
            "infinitive": "θεῖναι",
            "imperative": {
                "2nd singular": "θές",
                "2nd plural": "θέτε",
            },
            "participle": {
                "masculine": "θείς",
                "feminine": "θεῖσα",
                "neuter": "θέν",
            },
        },

        ("aorist", "middle"): {
            "indicative": [
                "ἐθέμην",
                "ἔθου",
                "ἔθετο",
                "ἐθέμεθα",
                "ἔθεσθε",
                "ἔθεντο",
            ],
            "infinitive": "θέσθαι",
            "imperative": {
                "2nd singular": "θοῦ",
                "2nd plural": "θέσθε",
            },
            "participle": {
                "masculine": "θέμενος",
                "feminine": "θεμένη",
                "neuter": "θέμενον",
            },
        },

        ("aorist", "passive"): {
            "indicative": [
                "ἐτέθην",
                "ἐτέθης",
                "ἐτέθη",
                "ἐτέθημεν",
                "ἐτέθητε",
                "ἐτέθησαν",
            ],
            "infinitive": "τεθῆναι",
            "imperative": {
                "2nd singular": "τέθητι",
                "2nd plural": "τέθητε",
            },
            "participle": {
                "masculine": "τεθείς",
                "feminine": "τεθεῖσα",
                "neuter": "τεθέν",
            },
        },

        ("perfect", "active"): {
            "indicative": [
                "τέθηκα",
                "τέθηκας",
                "τέθηκε(ν)",
                "τεθήκαμεν",
                "τεθήκατε",
                "τεθήκασι(ν)",
            ],
            "infinitive": "τεθηκέναι",
            "participle": {
                "masculine": "τεθηκώς",
                "feminine": "τεθηκυῖα",
                "neuter": "τεθηκός",
            },
        },

        ("perfect", "middle/passive"): {
            "indicative": [
                "τέθειμαι",
                "τέθεισαι",
                "τέθειται",
                "τεθείμεθα",
                "τέθεισθε",
                "τέθεινται",
            ],
            "infinitive": "τεθεῖσθαι",
            "participle": {
                "masculine": "τεθειμένος",
                "feminine": "τεθειμένη",
                "neuter": "τεθειμένον",
            },
        },
    },


    # ========================================================
    # δίδωμι
    # ========================================================

    "δίδωμι": {

        ("present", "active"): {
            "indicative": [
                "δίδωμι",
                "δίδως",
                "δίδωσι(ν)",
                "δίδομεν",
                "δίδοτε",
                "διδόασι(ν)",
            ],
            "infinitive": "διδόναι",
            "imperative": {
                "2nd singular": "δίδου",
                "2nd plural": "δίδοτε",
            },
            "participle": {
                "masculine": "διδούς",
                "feminine": "διδοῦσα",
                "neuter": "διδόν",
            },
        },

        ("present", "middle/passive"): {
            "indicative": [
                "δίδομαι",
                "δίδοσαι",
                "δίδοται",
                "διδόμεθα",
                "δίδοσθε",
                "δίδονται",
            ],
            "infinitive": "δίδοσθαι",
            "imperative": {
                "2nd singular": "δίδοσο",
                "2nd plural": "δίδοσθε",
            },
            "participle": {
                "masculine": "διδόμενος",
                "feminine": "διδομένη",
                "neuter": "διδόμενον",
            },
        },

        ("imperfect", "active"): {
            "indicative": [
                "ἐδίδουν",
                "ἐδίδους",
                "ἐδίδου",
                "ἐδίδομεν",
                "ἐδίδοτε",
                "ἐδίδοσαν",
            ],
        },

        ("imperfect", "middle/passive"): {
            "indicative": [
                "ἐδιδόμην",
                "ἐδίδοσο",
                "ἐδίδοτο",
                "ἐδιδόμεθα",
                "ἐδίδοσθε",
                "ἐδίδοντο",
            ],
        },

        ("future", "active"): {
            "indicative": [
                "δώσω",
                "δώσεις",
                "δώσει",
                "δώσομεν",
                "δώσετε",
                "δώσουσι(ν)",
            ],
            "infinitive": "δώσειν",
            "participle": {
                "masculine": "δώσων",
                "feminine": "δώσουσα",
                "neuter": "δῶσον",
            },
        },

        ("future", "middle"): {
            "indicative": [
                "δώσομαι",
                "δώσῃ",
                "δώσεται",
                "δωσόμεθα",
                "δώσεσθε",
                "δώσονται",
            ],
            "infinitive": "δώσεσθαι",
            "participle": {
                "masculine": "δωσόμενος",
                "feminine": "δωσομένη",
                "neuter": "δωσόμενον",
            },
        },

        ("future", "passive"): {
            "indicative": [
                "δοθήσομαι",
                "δοθήσῃ",
                "δοθήσεται",
                "δοθησόμεθα",
                "δοθήσεσθε",
                "δοθήσονται",
            ],
            "infinitive": "δοθήσεσθαι",
            "participle": {
                "masculine": "δοθησόμενος",
                "feminine": "δοθησομένη",
                "neuter": "δοθησόμενον",
            },
        },

        ("aorist", "active"): {
            "indicative": [
                "ἔδωκα",
                "ἔδωκας",
                "ἔδωκε(ν)",
                "ἔδομεν",
                "ἔδοτε",
                "ἔδοσαν",
            ],
            "infinitive": "δοῦναι",
            "imperative": {
                "2nd singular": "δός",
                "2nd plural": "δότε",
            },
            "participle": {
                "masculine": "δούς",
                "feminine": "δοῦσα",
                "neuter": "δόν",
            },
        },

        ("aorist", "middle"): {
            "indicative": [
                "ἐδόμην",
                "ἔδου",
                "ἔδοτο",
                "ἐδόμεθα",
                "ἔδοσθε",
                "ἔδοντο",
            ],
            "infinitive": "δόσθαι",
            "imperative": {
                "2nd singular": "δοῦ",
                "2nd plural": "δόσθε",
            },
            "participle": {
                "masculine": "δόμενος",
                "feminine": "δομένη",
                "neuter": "δόμενον",
            },
        },

        ("aorist", "passive"): {
            "indicative": [
                "ἐδόθην",
                "ἐδόθης",
                "ἐδόθη",
                "ἐδόθημεν",
                "ἐδόθητε",
                "ἐδόθησαν",
            ],
            "infinitive": "δοθῆναι",
            "imperative": {
                "2nd singular": "δόθητι",
                "2nd plural": "δόθητε",
            },
            "participle": {
                "masculine": "δοθείς",
                "feminine": "δοθεῖσα",
                "neuter": "δοθέν",
            },
        },

        ("perfect", "active"): {
            "indicative": [
                "δέδωκα",
                "δέδωκας",
                "δέδωκε(ν)",
                "δεδώκαμεν",
                "δεδώκατε",
                "δεδώκασι(ν)",
            ],
            "infinitive": "δεδωκέναι",
            "participle": {
                "masculine": "δεδωκώς",
                "feminine": "δεδωκυῖα",
                "neuter": "δεδωκός",
            },
        },

        ("perfect", "middle/passive"): {
            "indicative": [
                "δέδομαι",
                "δέδοσαι",
                "δέδοται",
                "δεδόμεθα",
                "δέδοσθε",
                "δέδονται",
            ],
            "infinitive": "δεδόσθαι",
            "participle": {
                "masculine": "δεδομένος",
                "feminine": "δεδομένη",
                "neuter": "δεδομένον",
            },
        },
    },

    # ========================================================
    # ἵστημι
    # ========================================================

    "ἵστημι": {

        ("present", "active"): {
            "indicative": [
                "ἵστημι",
                "ἵστης",
                "ἵστησι(ν)",
                "ἵσταμεν",
                "ἵστατε",
                "ἱστᾶσι(ν)",
            ],
            "infinitive": "ἱστάναι",
            "imperative": {
                "2nd singular": "ἵστη",
                "2nd plural": "ἵστατε",
            },
            "participle": {
                "masculine": "ἱστάς",
                "feminine": "ἱστᾶσα",
                "neuter": "ἱστάν",
            },
        },

        ("present", "middle/passive"): {
            "indicative": [
                "ἵσταμαι",
                "ἵστασαι",
                "ἵσταται",
                "ἱστάμεθα",
                "ἵστασθε",
                "ἵστανται",
            ],
            "infinitive": "ἵστασθαι",
            "imperative": {
                "2nd singular": "ἵστασο",
                "2nd plural": "ἵστασθε",
            },
            "participle": {
                "masculine": "ἱστάμενος",
                "feminine": "ἱσταμένη",
                "neuter": "ἱστάμενον",
            },
        },

        ("imperfect", "active"): {
            "indicative": [
                "ἵστην",
                "ἵστης",
                "ἵστη",
                "ἵσταμεν",
                "ἵστατε",
                "ἵστασαν",
            ],
        },

        ("imperfect", "middle/passive"): {
            "indicative": [
                "ἱστάμην",
                "ἵστασο",
                "ἵστατο",
                "ἱστάμεθα",
                "ἵστασθε",
                "ἵσταντο",
            ],
        },

        ("future", "active"): {
            "indicative": [
                "στήσω",
                "στήσεις",
                "στήσει",
                "στήσομεν",
                "στήσετε",
                "στήσουσι(ν)",
            ],
            "infinitive": "στήσειν",
            "participle": {
                "masculine": "στήσων",
                "feminine": "στήσουσα",
                "neuter": "στῆσον",
            },
        },

        ("future", "middle"): {
            "indicative": [
                "στήσομαι",
                "στήσῃ",
                "στήσεται",
                "στησόμεθα",
                "στήσεσθε",
                "στήσονται",
            ],
            "infinitive": "στήσεσθαι",
            "participle": {
                "masculine": "στησόμενος",
                "feminine": "στησομένη",
                "neuter": "στησόμενον",
            },
        },

        ("future", "passive"): {
            "indicative": [
                "σταθήσομαι",
                "σταθήσῃ",
                "σταθήσεται",
                "σταθησόμεθα",
                "σταθήσεσθε",
                "σταθήσονται",
            ],
            "infinitive": "σταθήσεσθαι",
            "participle": {
                "masculine": "σταθησόμενος",
                "feminine": "σταθησομένη",
                "neuter": "σταθησόμενον",
            },
        },

        ("aorist", "active"): {
            "indicative": [
                "ἔστησα",
                "ἔστησας",
                "ἔστησε(ν)",
                "ἐστήσαμεν",
                "ἐστήσατε",
                "ἔστησαν",
            ],
            "infinitive": "στῆσαι",
            "imperative": {
                "2nd singular": "στῆσον",
                "2nd plural": "στήσατε",
            },
            "participle": {
                "masculine": "στήσας",
                "feminine": "στήσασα",
                "neuter": "στῆσαν",
            },
        },

        ("aorist", "middle"): {
            "indicative": [
                "ἐστησάμην",
                "ἐστήσω",
                "ἐστήσατο",
                "ἐστησάμεθα",
                "ἐστήσασθε",
                "ἐστήσαντο",
            ],
            "infinitive": "στήσασθαι",
            "imperative": {
                "2nd singular": "στῆσαι",
                "2nd plural": "στήσασθε",
            },
            "participle": {
                "masculine": "στησάμενος",
                "feminine": "στησαμένη",
                "neuter": "στησάμενον",
            },
        },

        ("aorist", "passive"): {
            "indicative": [
                "ἐστάθην",
                "ἐστάθης",
                "ἐστάθη",
                "ἐστάθημεν",
                "ἐστάθητε",
                "ἐστάθησαν",
            ],
            "infinitive": "σταθῆναι",
            "imperative": {
                "2nd singular": "στάθητι",
                "2nd plural": "στάθητε",
            },
            "participle": {
                "masculine": "σταθείς",
                "feminine": "σταθεῖσα",
                "neuter": "σταθέν",
            },
        },

        ("2nd aorist", "active"): {
            "indicative": [
                "ἔστην",
                "ἔστης",
                "ἔστη",
                "ἔστημεν",
                "ἔστητε",
                "ἔστησαν",
            ],
            "infinitive": "στῆναι",
            "imperative": {
                "2nd singular": "στῆθι",
                "2nd plural": "στῆτε",
            },
            "participle": {
                "masculine": "στάς",
                "feminine": "στᾶσα",
                "neuter": "στάν",
            },
        },

        ("perfect", "active"): {
            "indicative": [
                "ἕστηκα",
                "ἕστηκας",
                "ἕστηκε(ν)",
                "ἑστήκαμεν",
                "ἑστήκατε",
                "ἑστήκασι(ν)",
            ],
            "infinitive": "ἑστηκέναι",
            "participle": {
                "masculine": "ἑστηκώς",
                "feminine": "ἑστηκυῖα",
                "neuter": "ἑστηκός",
            },
        },

        ("perfect", "middle/passive"): {
            "indicative": [
                "ἕσταμαι",
                "ἕστασαι",
                "ἕσταται",
                "ἑστάμεθα",
                "ἕστασθε",
                "ἕστανται",
            ],
        },
    },


    # ========================================================
    # ἵημι
    # ========================================================

    "ἵημι": {

        ("present", "active"): {
            "indicative": [
                "ἵημι",
                "ἵης",
                "ἵησι(ν)",
                "ἵεμεν",
                "ἵετε",
                "ἱᾶσι(ν)",
            ],
            "infinitive": "ἱέναι",
            "imperative": {
                "2nd singular": "ἵει",
                "2nd plural": "ἵετε",
            },
            "participle": {
                "masculine": "ἱείς",
                "feminine": "ἱεῖσα",
                "neuter": "ἱέν",
            },
        },

        ("present", "middle/passive"): {
            "indicative": [
                "ἵεμαι",
                "ἵεσαι",
                "ἵεται",
                "ἱέμεθα",
                "ἵεσθε",
                "ἵενται",
            ],
            "infinitive": "ἵεσθαι",
            "imperative": {
                "2nd singular": "ἵεσο",
                "2nd plural": "ἵεσθε",
            },
            "participle": {
                "masculine": "ἱέμενος",
                "feminine": "ἱεμένη",
                "neuter": "ἱέμενον",
            },
        },

        ("imperfect", "active"): {
            "indicative": [
                "ἵην",
                "ἵεις",
                "ἵει",
                "ἵεμεν",
                "ἵετε",
                "ἵεσαν",
            ],
        },

        ("imperfect", "middle/passive"): {
            "indicative": [
                "ἱέμην",
                "ἵεσο",
                "ἵετο",
                "ἱέμεθα",
                "ἵεσθε",
                "ἵεντο",
            ],
        },

        ("future", "active"): {
            "indicative": [
                "ἥσω",
                "ἥσεις",
                "ἥσει",
                "ἥσομεν",
                "ἥσετε",
                "ἥσουσι(ν)",
            ],
            "infinitive": "ἥσειν",
            "participle": {
                "masculine": "ἥσων",
                "feminine": "ἥσουσα",
                "neuter": "ἧσον",
            },
        },

        ("future", "middle"): {
            "indicative": [
                "ἥσομαι",
                "ἥσῃ",
                "ἥσεται",
                "ἡσόμεθα",
                "ἥσεσθε",
                "ἥσονται",
            ],
            "infinitive": "ἥσεσθαι",
            "participle": {
                "masculine": "ἡσόμενος",
                "feminine": "ἡσομένη",
                "neuter": "ἡσόμενον",
            },
        },

        ("future", "passive"): {
            "indicative": [
                "ἑθήσομαι",
                "ἑθήσῃ",
                "ἑθήσεται",
                "ἑθησόμεθα",
                "ἑθήσεσθε",
                "ἑθήσονται",
            ],
            "infinitive": "ἑθήσεσθαι",
            "participle": {
                "masculine": "ἑθησόμενος",
                "feminine": "ἑθησομένη",
                "neuter": "ἑθησόμενον",
            },
        },

        ("aorist", "active"): {
            "indicative": [
                "ἧκα",
                "ἧκας",
                "ἧκε(ν)",
                "εἷμεν",
                "εἷτε",
                "εἷσαν",
            ],
            "infinitive": "εἷναι",
            "imperative": {
                "2nd singular": "ἕς",
                "2nd plural": "ἕτε",
            },
            "participle": {
                "masculine": "εἷς",
                "feminine": "εἷσα",
                "neuter": "ἕν",
            },
        },

        ("aorist", "middle"): {
            "indicative": [
                "εἵμην",
                "εἷσο",
                "εἷτο",
                "εἵμεθα",
                "εἷσθε",
                "εἷντο",
            ],
            "infinitive": "ἕσθαι",
            "imperative": {
                "2nd singular": "οὗ",
                "2nd plural": "ἕσθε",
            },
            "participle": {
                "masculine": "ἕμενος",
                "feminine": "ἑμένη",
                "neuter": "ἕμενον",
            },
        },

        ("aorist", "passive"): {
            "indicative": [
                "εἵθην",
                "εἵθης",
                "εἵθη",
                "εἵθημεν",
                "εἵθητε",
                "εἵθησαν",
            ],
            "infinitive": "εἰθῆναι",
            "imperative": {
                "2nd singular": "εἵθητι",
                "2nd plural": "εἵθητε",
            },
            "participle": {
                "masculine": "εἱθείς",
                "feminine": "εἱθεῖσα",
                "neuter": "εἱθέν",
            },
        },

        ("perfect", "active"): {
            "indicative": [
                "εἷκα",
                "εἷκας",
                "εἷκε(ν)",
                "εἵκαμεν",
                "εἵκατε",
                "εἵκασι(ν)",
            ],
            "infinitive": "εἱκέναι",
            "participle": {
                "masculine": "εἱκώς",
                "feminine": "εἱκυῖα",
                "neuter": "εἱκός",
            },
        },

        ("perfect", "middle/passive"): {
            "indicative": [
                "εἷμαι",
                "εἷσαι",
                "εἷται",
                "εἵμεθα",
                "εἷσθε",
                "εἷνται",
            ],
        },
    },
}


# ============================================================
# BUILD QUIZ ITEMS
# ============================================================

def build_items(verb, selected_keys, selected_form_types):
    items = []

    paradigms = VERBS[verb]

    for key in selected_keys:
        tense, voice = key
        data = paradigms[key]

        # ---------------- Indicatives ----------------

        if "Indicative" in selected_form_types and "indicative" in data:
            for i, form in enumerate(data["indicative"]):
                items.append({
                    "form": form,
                    "parse_label":
                        f"{PERSONS[i]}, {tense} {voice} indicative",
                })

        # ---------------- Infinitives ----------------

        if "Infinitive" in selected_form_types and "infinitive" in data:
            items.append({
                "form": data["infinitive"],
                "parse_label":
                    f"{tense} {voice} infinitive",
            })

        # ---------------- Imperatives ----------------

        if "Imperative" in selected_form_types and "imperative" in data:
            for person, form in data["imperative"].items():
                items.append({
                    "form": form,
                    "parse_label":
                        f"{person}, {tense} {voice} imperative",
                })

        # ---------------- Participles ----------------

        if "Participle" in selected_form_types and "participle" in data:
            for gender, form in data["participle"].items():
                items.append({
                    "form": form,
                    "parse_label":
                        f"{tense} {voice} participle, "
                        f"{gender} nominative singular",
                })

    return items


# ============================================================
# PAGE SETUP
# ============================================================

st.set_page_config(
    page_title="Ancient Greek Drill Tool",
    layout="centered"
)

st.title("Ancient Greek Drill Tool")


# ============================================================
# VERB SELECTION
# ============================================================

verb = st.selectbox(
    "Verb",
    options=list(VERBS.keys())
)

st.subheader(f"Verb: {verb}")


# ============================================================
# DIRECTION
# ============================================================

mode = st.radio(
    "Direction",
    [
        "Greek → parse",
        "English → Greek",
    ],
    horizontal=True
)


# ============================================================
# PARADIGM SELECTION
# ============================================================

available_keys = list(VERBS[verb].keys())

all_paradigm_labels = [
    f"{tense} {voice}"
    for tense, voice in available_keys
]

label_to_key = {
    f"{tense} {voice}": (tense, voice)
    for tense, voice in available_keys
}

selected_labels = st.multiselect(
    "Choose paradigms",
    options=all_paradigm_labels,
    default=all_paradigm_labels
)


# ============================================================
# FORM TYPE SELECTION
# ============================================================

selected_form_types = st.multiselect(
    "Choose forms",
    options=FORM_TYPES,
    default=FORM_TYPES
)


# ============================================================
# QUIZ SETTINGS
# ============================================================

num_prompts = st.slider(
    "Number of prompts",
    1,
    30,
    10
)

allow_repeats = st.checkbox(
    "Allow repeated prompts",
    value=False
)


# ============================================================
# SESSION STATE
# ============================================================

if "quiz" not in st.session_state:
    st.session_state.quiz = None

if "revealed" not in st.session_state:
    st.session_state.revealed = False

if "quiz_mode" not in st.session_state:
    st.session_state.quiz_mode = mode

if "quiz_verb" not in st.session_state:
    st.session_state.quiz_verb = verb


# ============================================================
# GENERATE QUIZ
# ============================================================

if st.button("Generate quiz"):

    selected_keys = [
        label_to_key[label]
        for label in selected_labels
    ]

    items = build_items(
        verb,
        selected_keys,
        selected_form_types
    )

    if not selected_keys:
        st.warning("Please select at least one paradigm.")

    elif not selected_form_types:
        st.warning("Please select at least one form type.")

    elif not items:
        st.warning(
            "There are no forms matching those selections."
        )

    else:
        if allow_repeats:
            quiz = [
                random.choice(items)
                for _ in range(num_prompts)
            ]
        else:
            sample_size = min(
                num_prompts,
                len(items)
            )
            quiz = random.sample(
                items,
                sample_size
            )

        st.session_state.quiz = quiz
        st.session_state.revealed = False

        # Store these so changing controls after generating
        # doesn't change an already-generated sheet.
        st.session_state.quiz_mode = mode
        st.session_state.quiz_verb = verb


# ============================================================
# DISPLAY QUIZ
# ============================================================

quiz = st.session_state.quiz

if quiz:

    quiz_mode = st.session_state.quiz_mode
    quiz_verb = st.session_state.quiz_verb

    st.markdown("## Quiz")
    st.caption(f"Verb: {quiz_verb}")

    for i, item in enumerate(quiz, start=1):

        if quiz_mode == "Greek → parse":
            st.write(
                f"{i}. **{item['form']}**"
            )

        else:
            st.write(
                f"{i}. **{item['parse_label']}**"
            )

    if st.button("Reveal answers"):
        st.session_state.revealed = True


# ============================================================
# ANSWER KEY
# ============================================================

if quiz and st.session_state.revealed:

    quiz_mode = st.session_state.quiz_mode

    st.markdown("## Answer key")

    for i, item in enumerate(quiz, start=1):

        if quiz_mode == "Greek → parse":
            st.write(
                f"{i}. **{item['form']}** "
                f"→ {item['parse_label']}"
            )

        else:
            st.write(
                f"{i}. **{item['parse_label']}** "
                f"→ {item['form']}"
            )
