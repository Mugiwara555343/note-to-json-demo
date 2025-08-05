# 📝 Note-to-json-demo 📁

> Markdown memory logs → structured `.json` with live file watching 🧠

This is a standalone demo of the **Markdown-to-JSON memory parser** and **file change watcher** used in the AI Memory Architecture project. It converts `.md` logs into clean `.parsed.json` objects with metadata, summaries, and core reflections.

You can:
- 📝 Write or edit markdown memory entries
- ⚙️ Parse them into structured `.parsed.json` snapshots
- 👁️ Enable live file watching (auto-parse on edit)

---

## 📦 What's Inside

| File                | Role                                         |
|---------------------|----------------------------------------------|
| `memory_parser.py`  | Parses `.md` files → `.parsed.json`          |
| `memory_watcher.py` | Watches folder for `.md` edits, auto-parses  |
| `run_demo.py`       | Manually parse all `.md` files in the folder |
| `run_demo.bat`      | Windows batch file to run the demo            |
| `start_watcher.bat` | Windows batch file to start the watcher       |
| `demo_entries/`     | Folder with 5 sample logs for testing        |
| `watch_config.json` | Declares which folders the watcher monitors  |
| `requirements.txt`  | Installs `watchdog` and `jsonschema`         |

### 🧪 Demo Entries

The `demo_entries/` folder contains 5 sample markdown files showcasing different emotional tones:
- `demo_entry.md` - Reflective morning entry
- `creative_breakthrough.md` - Enthusiastic breakthrough moment
- `frustration_moment.md` - Frustrated debugging session
- `peaceful_morning.md` - Calm gratitude practice
- `team_collaboration.md` - Energized team meeting

---

## 🚀 How to Use

### 1. Clone the Repository

git clone https://github.com/Mugiwara555343/note-to-json-demo.git
cd note-to-json-demo

---

### 2. Install Dependencies

pip install -r requirements.txt

---

### 3. Manual Parse (Run Once)

**Option A: Command Line**
```bash
python run_demo.py
```

**Option B: Windows (Double-click)**
```
run_demo.bat
```

✅ This will convert all `.md` files in the `demo_entries/` folder to `.parsed.json` files.

---

### 4. Enable Live Watching (Auto Mode)

**Option A: Command Line**
```bash
python memory_watcher.py
```

**Option B: Windows (Double-click)**
```
start_watcher.bat
```

Now edit any `.md` file in the `demo_entries/` folder (or add new ones).

✅ On save, the watcher re-runs the parser and updates/creates the corresponding `.parsed.json`.

---

## 🧪 Output Example

After parsing, you’ll get:

{
  "title": "Morning Reflection",
  "timestamp": "2025-07-17T20:18:21Z",
  "summary": "Today I spent time refining the AI memory watcher...",
  "tags": ["focus", "emotion", "ai"],
  "reflections": [
    "Resilience is built through iteration.",
    "System design is emotional memory made technical."
  ]
}

---

## 📝 Markdown Format

Your `.md` files should follow this structure:

```markdown
# Title
**Date:** YYYY-MM-DD  
**Tags:** #tag1 #tag2 #tag3  
**Tone:** Emotional tone

**Summary:**
Brief summary of the entry.

**Core Reflections:**
- First reflection point
- Second reflection point
- Third reflection point
```

## 📌 Notes

- `.parsed.json` is stored in the same folder as the `.md` file
- Files that fail schema validation will be skipped with a warning
- Watching behavior is debounced to avoid duplicate triggering
- The parser extracts: title, date, tags, tone, summary, and reflections
- All fields are optional except title, timestamp, raw_text, and plain_text

---

## 📜 License

MIT — free to use, modify, and extend.

---
### 🔄 Related Work
* **Legacy-AMA (v1, archived)** – full pipeline prototype  
* **AMA v2 (private, in progress)** – orchestration, GPU router, RAG

