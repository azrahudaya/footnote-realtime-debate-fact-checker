# Footnote: Realtime Debate Fact Checker

every claim, sourced.

Footnote listens to a debate while you watch it, writes a live transcript on your own GPU, picks out the factual claims, and checks each one against sources you can open. Every verdict comes with a short reason and the quotes it relies on. When the evidence is thin, Footnote says it cannot verify the claim instead of guessing.

It runs entirely on your machine. The only data that leaves it is what you choose to send: claim text to your LLM endpoint, and search queries to the evidence providers you enable.

## What you need

- Linux with an NVIDIA GPU (developed on Ubuntu 26.04 with an RTX 3050 6 GB). Without a GPU, transcription falls back to the CPU with a smaller model.
- Python 3.12, [uv](https://docs.astral.sh/uv/), Node.js 22 with corepack, and FFmpeg (`sudo apt install ffmpeg`).
- An OpenAI-compatible LLM endpoint and its API key. The default base URL is `http://localhost:20128/v1`.
- Optional: API keys for [Tavily](https://tavily.com) (search) and [Firecrawl](https://firecrawl.dev) (page fetching). Without them, Footnote searches Wikipedia only.

Windows should work but is not tested yet. macOS is not supported.

## Run it

```bash
git clone https://github.com/azrahudaya/footnote-realtime-debate-fact-checker.git
cd footnote-realtime-debate-fact-checker
scripts/dev-setup
pnpm dev
```

Open http://127.0.0.1:5173. The first start downloads the speech model (about 1.6 GB).

To run without the development servers, use `pnpm start` and open http://127.0.0.1:8765.

`uv run footnote doctor` checks FFmpeg, CUDA, the speech model, and your LLM endpoint, and tells you what to fix.

## Configure

Open **Pengaturan** (Settings) in the app:

1. **LLM:** set the base URL and API key, then pick two models from the list your endpoint reports: a fast one for finding claims and a stronger one for checking them. **Test koneksi** shows whether each model supports structured output.
2. **Sumber bukti:** add your Tavily and Firecrawl keys and choose which providers to use.
3. **STT:** pick the speech model and language. For debates that mix Indonesian and English, keep the language set to Indonesian.

Keys are stored in `~/.local/share/footnote/secrets.toml`, readable only by your user, and never written to logs. Other settings can also be set in `~/.config/footnote/config.toml` or with `FOOTNOTE_*` environment variables.

## Sources Footnote can read

- YouTube videos and live streams
- Stream URLs: HLS (`.m3u8`), DASH, RTMP, direct video or audio files
- Files you upload
- Your microphone or system audio (PipeWire or PulseAudio monitor)

## Limitations

- Verdicts are machine-assisted and can be wrong. Read the sources before you rely on one.
- Transcription quality drops with heavy accents, regional languages, and people talking over each other.
- Speaker labels are set by hand for now.
- One session runs at a time.
- Downloading YouTube audio may conflict with YouTube's terms of service. Footnote processes audio locally for personal analysis, never stores the video, and does not support signed-in YouTube sessions.
- Recording a microphone may capture people who have not agreed to it. Ask first.

## License

Apache License 2.0. See [LICENSE](LICENSE), [NOTICE](NOTICE), and [THIRD_PARTY_LICENSES](THIRD_PARTY_LICENSES).

How it works: [docs/architecture.md](docs/architecture.md).
