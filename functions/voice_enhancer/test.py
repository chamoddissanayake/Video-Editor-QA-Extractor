from utils.assembly_ai.speech_to_text import get_lecturer_transcription
from topic_extractor import topic_extractor as tp

arr = [
    {
        "text": "Hello.",
        "confidence": 0.99,
        "speaker": "A",
        "end": 2820,
        "start": 1820
    },
    {
        "text": "Good",
        "confidence": 0.95,
        "speaker": "A",
        "end": 3420,
        "start": 2880
    },
    {
        "text": "afternoon.",
        "confidence": 0.93,
        "speaker": "A",
        "end": 3930,
        "start": 3430
    },
    {
        "text": "Okay.",
        "confidence": 0.97,
        "speaker": "A",
        "end": 7180,
        "start": 6180
    },
    {
        "text": "Can",
        "confidence": 1.0,
        "speaker": "A",
        "end": 10130,
        "start": 9140
    },
    {
        "text": "you",
        "confidence": 0.99,
        "speaker": "A",
        "end": 10340,
        "start": 10140
    },
    {
        "text": "hear",
        "confidence": 0.95,
        "speaker": "A",
        "end": 10580,
        "start": 10350
    },
    {
        "text": "me?",
        "confidence": 0.99,
        "speaker": "A",
        "end": 10700,
        "start": 10590
    },
    {
        "text": "Okay.",
        "confidence": 0.99,
        "speaker": "A",
        "end": 15110,
        "start": 14110
    },
    {
        "text": "Thanks.",
        "confidence": 0.81,
        "speaker": "A",
        "end": 16130,
        "start": 15380
    },
    {
        "text": "Okay.",
        "confidence": 0.87,
        "speaker": "A",
        "end": 17320,
        "start": 16780
    },
    {
        "text": "A",
        "confidence": 0.97,
        "speaker": "A",
        "end": 18100,
        "start": 17330
    },
    {
        "text": "few",
        "confidence": 0.94,
        "speaker": "A",
        "end": 18430,
        "start": 18100
    },
    {
        "text": "more",
        "confidence": 0.93,
        "speaker": "A",
        "end": 18670,
        "start": 18440
    },
    {
        "text": "to",
        "confidence": 1.0,
        "speaker": "A",
        "end": 18820,
        "start": 18680
    },
    {
        "text": "join,",
        "confidence": 0.97,
        "speaker": "A",
        "end": 19090,
        "start": 18830
    },
    {
        "text": "but",
        "confidence": 0.99,
        "speaker": "A",
        "end": 19390,
        "start": 19180
    },
    {
        "text": "I",
        "confidence": 1.0,
        "speaker": "A",
        "end": 19450,
        "start": 19400
    },
    {
        "text": "think",
        "confidence": 0.93,
        "speaker": "A",
        "end": 20020,
        "start": 19630
    },
    {
        "text": "Let's",
        "confidence": 0.9,
        "speaker": "A",
        "end": 20770,
        "start": 20110
    },
    {
        "text": "start",
        "confidence": 0.96,
        "speaker": "A",
        "end": 21010,
        "start": 20780
    },
    {
        "text": "they",
        "confidence": 0.95,
        "speaker": "A",
        "end": 21610,
        "start": 21040
    },
    {
        "text": "will",
        "confidence": 0.95,
        "speaker": "A",
        "end": 21940,
        "start": 21620
    },
    {
        "text": "join.",
        "confidence": 0.96,
        "speaker": "A",
        "end": 22240,
        "start": 21940
    },
    {
        "text": "I",
        "confidence": 1.0,
        "speaker": "A",
        "end": 23260,
        "start": 23140
    },
    {
        "text": "think",
        "confidence": 0.96,
        "speaker": "A",
        "end": 26140,
        "start": 25140
    },
    {
        "text": "we",
        "confidence": 0.9,
        "speaker": "A",
        "end": 26680,
        "start": 26320
    },
    {
        "text": "have",
        "confidence": 0.95,
        "speaker": "A",
        "end": 27130,
        "start": 26860
    },
    {
        "text": "done",
        "confidence": 0.97,
        "speaker": "A",
        "end": 27430,
        "start": 27130
    },
    {
        "text": "a",
        "confidence": 0.99,
        "speaker": "A",
        "end": 27670,
        "start": 27550
    },
    {
        "text": "few",
        "confidence": 0.92,
        "speaker": "A",
        "end": 27970,
        "start": 27670
    },
    {
        "text": "a",
        "confidence": 0.87,
        "speaker": "A",
        "end": 28800,
        "start": 28680
    },
    {
        "text": "few",
        "confidence": 0.78,
        "speaker": "A",
        "end": 30090,
        "start": 29700
    },
    {
        "text": "analytics",
        "confidence": 0.87,
        "speaker": "A",
        "end": 30600,
        "start": 30100
    },
    {
        "text": "related",
        "confidence": 0.91,
        "speaker": "A",
        "end": 31140,
        "start": 30610
    },
    {
        "text": "topics",
        "confidence": 0.94,
        "speaker": "A",
        "end": 31590,
        "start": 31150
    },
    {
        "text": "in",
        "confidence": 0.95,
        "speaker": "A",
        "end": 31830,
        "start": 31590
    },
    {
        "text": "previous",
        "confidence": 0.95,
        "speaker": "A",
        "end": 32430,
        "start": 31840
    },
    {
        "text": "lectures.",
        "confidence": 0.92,
        "speaker": "A",
        "end": 32940,
        "start": 32430
    },
    {
        "text": "So",
        "confidence": 0.93,
        "speaker": "A",
        "end": 33240,
        "start": 32970
    },
    {
        "text": "we",
        "confidence": 0.95,
        "speaker": "A",
        "end": 33420,
        "start": 33250
    },
    {
        "text": "need",
        "confidence": 0.78,
        "speaker": "A",
        "end": 33750,
        "start": 33430
    },
    {
        "text": "Association",
        "confidence": 0.93,
        "speaker": "A",
        "end": 35040,
        "start": 34040
    },
    {
        "text": "related",
        "confidence": 0.89,
        "speaker": "A",
        "end": 35640,
        "start": 35130
    },
    {
        "text": "things,",
        "confidence": 0.9,
        "speaker": "A",
        "end": 36030,
        "start": 35640
    },
    {
        "text": "then",
        "confidence": 0.87,
        "speaker": "A",
        "end": 36420,
        "start": 36150
    },
    {
        "text": "classification",
        "confidence": 0.92,
        "speaker": "A",
        "end": 37470,
        "start": 36430
    },
    {
        "text": "some",
        "confidence": 0.89,
        "speaker": "A",
        "end": 37800,
        "start": 37500
    },
    {
        "text": "algorithms",
        "confidence": 0.91,
        "speaker": "A",
        "end": 38520,
        "start": 37810
    },
    {
        "text": "and",
        "confidence": 0.97,
        "speaker": "A",
        "end": 38730,
        "start": 38530
    },
    {
        "text": "then",
        "confidence": 0.98,
        "speaker": "A",
        "end": 38970,
        "start": 38740
    },
    {
        "text": "cluster",
        "confidence": 0.9,
        "speaker": "A",
        "end": 40080,
        "start": 39510
    },
    {
        "text": "in",
        "confidence": 0.91,
        "speaker": "A",
        "end": 40230,
        "start": 40090
    },
    {
        "text": "one",
        "confidence": 0.97,
        "speaker": "A",
        "end": 40440,
        "start": 40240
    },
    {
        "text": "of",
        "confidence": 0.98,
        "speaker": "A",
        "end": 40590,
        "start": 40450
    },
    {
        "text": "the",
        "confidence": 0.98,
        "speaker": "A",
        "end": 40740,
        "start": 40600
    },
    {
        "text": "algorithm.",
        "confidence": 0.93,
        "speaker": "A",
        "end": 41250,
        "start": 40750
    },
    {
        "text": "So",
        "confidence": 0.99,
        "speaker": "A",
        "end": 43010,
        "start": 42010
    },
    {
        "text": "basic",
        "confidence": 0.96,
        "speaker": "A",
        "end": 43670,
        "start": 43020
    },
    {
        "text": "things",
        "confidence": 0.95,
        "speaker": "A",
        "end": 44420,
        "start": 44030
    },
    {
        "text": "related",
        "confidence": 0.95,
        "speaker": "A",
        "end": 44990,
        "start": 44450
    },
    {
        "text": "to",
        "confidence": 0.95,
        "speaker": "A",
        "end": 45200,
        "start": 45020
    },
    {
        "text": "analytics",
        "confidence": 0.97,
        "speaker": "A",
        "end": 48000,
        "start": 47000
    },
    {
        "text": "we",
        "confidence": 0.91,
        "speaker": "A",
        "end": 48180,
        "start": 48010
    },
    {
        "text": "have",
        "confidence": 0.98,
        "speaker": "A",
        "end": 48510,
        "start": 48190
    },
    {
        "text": "done.",
        "confidence": 0.97,
        "speaker": "A",
        "end": 48810,
        "start": 48520
    },
    {
        "text": "But",
        "confidence": 0.91,
        "speaker": "A",
        "end": 49140,
        "start": 48930
    },
    {
        "text": "when",
        "confidence": 0.97,
        "speaker": "A",
        "end": 50400,
        "start": 49860
    },
    {
        "text": "we",
        "confidence": 0.97,
        "speaker": "A",
        "end": 50550,
        "start": 50410
    },
    {
        "text": "look",
        "confidence": 0.96,
        "speaker": "A",
        "end": 50880,
        "start": 50560
    },
    {
        "text": "at",
        "confidence": 0.94,
        "speaker": "A",
        "end": 51090,
        "start": 50880
    },
    {
        "text": "life",
        "confidence": 0.98,
        "speaker": "A",
        "end": 52590,
        "start": 51590
    },
    {
        "text": "cycle",
        "confidence": 0.94,
        "speaker": "A",
        "end": 53070,
        "start": 52620
    },
    {
        "text": "of",
        "confidence": 0.99,
        "speaker": "A",
        "end": 53370,
        "start": 53190
    },
    {
        "text": "analytics",
        "confidence": 0.93,
        "speaker": "A",
        "end": 54000,
        "start": 53380
    },
    {
        "text": "related",
        "confidence": 0.87,
        "speaker": "A",
        "end": 54570,
        "start": 54000
    },
    {
        "text": "projects,",
        "confidence": 0.95,
        "speaker": "A",
        "end": 54990,
        "start": 54570
    },
    {
        "text": "so",
        "confidence": 1.0,
        "speaker": "A",
        "end": 55310,
        "start": 55160
    },
    {
        "text": "we",
        "confidence": 0.93,
        "speaker": "A",
        "end": 56090,
        "start": 55730
    },
    {
        "text": "want",
        "confidence": 0.96,
        "speaker": "A",
        "end": 56420,
        "start": 56150
    },
    {
        "text": "to",
        "confidence": 0.84,
        "speaker": "A",
        "end": 56570,
        "start": 56430
    },
    {
        "text": "do",
        "confidence": 0.98,
        "speaker": "A",
        "end": 56720,
        "start": 56580
    },
    {
        "text": "the",
        "confidence": 0.98,
        "speaker": "A",
        "end": 57020,
        "start": 56730
    },
    {
        "text": "data",
        "confidence": 0.94,
        "speaker": "A",
        "end": 57320,
        "start": 57030
    },
    {
        "text": "of",
        "confidence": 0.67,
        "speaker": "A",
        "end": 57470,
        "start": 57330
    },
    {
        "text": "preprocessing",
        "confidence": 0.91,
        "speaker": "A",
        "end": 58400,
        "start": 57500
    },
    {
        "text": "area.",
        "confidence": 0.85,
        "speaker": "A",
        "end": 58970,
        "start": 58490
    },
    {
        "text": "So",
        "confidence": 1.0,
        "speaker": "A",
        "end": 60210,
        "start": 59340
    },
    {
        "text": "therefore,",
        "confidence": 0.89,
        "speaker": "A",
        "end": 60930,
        "start": 60270
    },
    {
        "text": "I",
        "confidence": 1.0,
        "speaker": "A",
        "end": 61050,
        "start": 60940
    },
    {
        "text": "thought",
        "confidence": 0.8,
        "speaker": "A",
        "end": 61620,
        "start": 61110
    },
    {
        "text": "of",
        "confidence": 0.86,
        "speaker": "A",
        "end": 61830,
        "start": 61620
    },
    {
        "text": "talking",
        "confidence": 0.94,
        "speaker": "A",
        "end": 62820,
        "start": 61840
    },
    {
        "text": "about",
        "confidence": 0.92,
        "speaker": "A",
        "end": 63240,
        "start": 62880
    },
    {
        "text": "some",
        "confidence": 0.96,
        "speaker": "A",
        "end": 64590,
        "start": 64200
    },
    {
        "text": "technique",
        "confidence": 0.86,
        "speaker": "A",
        "end": 65160,
        "start": 64590
    },
    {
        "text": "related",
        "confidence": 0.88,
        "speaker": "A",
        "end": 65670,
        "start": 65190
    },
    {
        "text": "to",
        "confidence": 0.79,
        "speaker": "A",
        "end": 65820,
        "start": 65680
    },
    {
        "text": "data",
        "confidence": 0.92,
        "speaker": "A",
        "end": 66150,
        "start": 65830
    },
    {
        "text": "preprocessing",
        "confidence": 0.93,
        "speaker": "A",
        "end": 67020,
        "start": 66150
    },
    {
        "text": "in",
        "confidence": 0.83,
        "speaker": "A",
        "end": 67200,
        "start": 67020
    },
    {
        "text": "this",
        "confidence": 0.89,
        "speaker": "A",
        "end": 67440,
        "start": 67210
    },
    {
        "text": "lecture,",
        "confidence": 0.8,
        "speaker": "A",
        "end": 67860,
        "start": 67450
    },
    {
        "text": "Let's",
        "confidence": 0.74,
        "speaker": "A",
        "end": 69390,
        "start": 69030
    },
    {
        "text": "see",
        "confidence": 0.96,
        "speaker": "A",
        "end": 69570,
        "start": 69400
    },
    {
        "text": "some",
        "confidence": 0.99,
        "speaker": "A",
        "end": 71230,
        "start": 70180
    },
    {
        "text": "of",
        "confidence": 0.99,
        "speaker": "A",
        "end": 71380,
        "start": 71240
    },
    {
        "text": "the",
        "confidence": 0.96,
        "speaker": "A",
        "end": 71680,
        "start": 71390
    },
    {
        "text": "techniques",
        "confidence": 0.96,
        "speaker": "A",
        "end": 72370,
        "start": 71690
    },
    {
        "text": "we",
        "confidence": 0.97,
        "speaker": "A",
        "end": 72580,
        "start": 72380
    },
    {
        "text": "use",
        "confidence": 0.92,
        "speaker": "A",
        "end": 72880,
        "start": 72590
    },
    {
        "text": "data",
        "confidence": 0.94,
        "speaker": "A",
        "end": 74410,
        "start": 73410
    },
    {
        "text": "preprocessing.",
        "confidence": 0.83,
        "speaker": "A",
        "end": 75220,
        "start": 74410
    },
    {
        "text": "So",
        "confidence": 0.9,
        "speaker": "A",
        "end": 75400,
        "start": 75220
    },
    {
        "text": "before",
        "confidence": 0.95,
        "speaker": "A",
        "end": 76330,
        "start": 75410
    },
    {
        "text": "we",
        "confidence": 0.91,
        "speaker": "A",
        "end": 76540,
        "start": 76330
    },
    {
        "text": "use,",
        "confidence": 0.97,
        "speaker": "A",
        "end": 76870,
        "start": 76630
    },
    {
        "text": "use",
        "confidence": 0.98,
        "speaker": "A",
        "end": 77720,
        "start": 77180
    },
    {
        "text": "our",
        "confidence": 0.95,
        "speaker": "A",
        "end": 78020,
        "start": 77750
    },
    {
        "text": "data",
        "confidence": 0.9,
        "speaker": "A",
        "end": 78320,
        "start": 78020
    },
    {
        "text": "with",
        "confidence": 0.89,
        "speaker": "A",
        "end": 78620,
        "start": 78320
    },
    {
        "text": "the",
        "confidence": 0.58,
        "speaker": "A",
        "end": 78860,
        "start": 78650
    },
    {
        "text": "modules,",
        "confidence": 0.91,
        "speaker": "A",
        "end": 79970,
        "start": 79460
    },
    {
        "text": "so",
        "confidence": 0.97,
        "speaker": "A",
        "end": 80850,
        "start": 80400
    },
    {
        "text": "we",
        "confidence": 0.89,
        "speaker": "A",
        "end": 81030,
        "start": 80860
    },
    {
        "text": "want",
        "confidence": 0.97,
        "speaker": "A",
        "end": 81360,
        "start": 81060
    },
    {
        "text": "to",
        "confidence": 0.99,
        "speaker": "A",
        "end": 81630,
        "start": 81370
    },
    {
        "text": "do",
        "confidence": 0.92,
        "speaker": "A",
        "end": 81810,
        "start": 81640
    },
    {
        "text": "some",
        "confidence": 0.98,
        "speaker": "A",
        "end": 82590,
        "start": 81820
    },
    {
        "text": "for",
        "confidence": 0.91,
        "speaker": "A",
        "end": 83850,
        "start": 83400
    },
    {
        "text": "the",
        "confidence": 0.84,
        "speaker": "A",
        "end": 84090,
        "start": 83860
    },
    {
        "text": "processing",
        "confidence": 0.94,
        "speaker": "A",
        "end": 84690,
        "start": 84090
    },
    {
        "text": "and",
        "confidence": 0.93,
        "speaker": "A",
        "end": 84930,
        "start": 84700
    },
    {
        "text": "prepare",
        "confidence": 0.96,
        "speaker": "A",
        "end": 85560,
        "start": 84940
    },
    {
        "text": "our",
        "confidence": 0.82,
        "speaker": "A",
        "end": 85860,
        "start": 85570
    },
    {
        "text": "data",
        "confidence": 0.92,
        "speaker": "A",
        "end": 86160,
        "start": 85870
    },
    {
        "text": "sets",
        "confidence": 0.85,
        "speaker": "A",
        "end": 86520,
        "start": 86170
    },
    {
        "text": "to",
        "confidence": 0.98,
        "speaker": "A",
        "end": 87450,
        "start": 86520
    },
    {
        "text": "fit",
        "confidence": 0.83,
        "speaker": "A",
        "end": 87810,
        "start": 87540
    },
    {
        "text": "into",
        "confidence": 0.88,
        "speaker": "A",
        "end": 88170,
        "start": 87840
    },
    {
        "text": "data",
        "confidence": 0.93,
        "speaker": "A",
        "end": 88500,
        "start": 88180
    },
    {
        "text": "models.",
        "confidence": 0.95,
        "speaker": "A",
        "end": 88830,
        "start": 88500
    },
    {
        "text": "So",
        "confidence": 1.0,
        "speaker": "A",
        "end": 89230,
        "start": 89080
    },
    {
        "text": "some",
        "confidence": 0.96,
        "speaker": "A",
        "end": 91060,
        "start": 90060
    },
    {
        "text": "of",
        "confidence": 0.96,
        "speaker": "A",
        "end": 91180,
        "start": 91070
    },
    {
        "text": "the",
        "confidence": 0.66,
        "speaker": "A",
        "end": 91360,
        "start": 91190
    },
    {
        "text": "things",
        "confidence": 0.94,
        "speaker": "A",
        "end": 91660,
        "start": 91370
    },
    {
        "text": "we",
        "confidence": 1.0,
        "speaker": "A",
        "end": 91780,
        "start": 91670
    },
    {
        "text": "can",
        "confidence": 0.99,
        "speaker": "A",
        "end": 92080,
        "start": 91840
    },
    {
        "text": "discuss",
        "confidence": 0.93,
        "speaker": "A",
        "end": 92500,
        "start": 92090
    },
    {
        "text": "with",
        "confidence": 0.92,
        "speaker": "A",
        "end": 92770,
        "start": 92510
    },
    {
        "text": "decision.",
        "confidence": 0.86,
        "speaker": "A",
        "end": 93370,
        "start": 92780
    }
]
transcription = get_lecturer_transcription(arr)

tp.topic_extractor(transcription)
