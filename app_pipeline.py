

async def run_pipeline(keywords, themes, regions, max_results, num_random, custom_prompt=None):
    OUTPUT_FILE = "final_transcript_story.txt"
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    for keyword in keywords:
        for region_code in regions:
            videos = search_youtube_videos_by_keyword(keyword, max_results=max_results, region_code=region_code)
            if not videos:
                continue
            selected_videos = random.sample(videos, min(num_random, len(videos)))
            for title, description, url in selected_videos:
                video_id = url.split("v=")[-1]
                audio_file = download_audio(url, output_basename=video_id)
                if not audio_file:
                    continue
                transcript = transcribe_audio(audio_file)
                if not transcript or len(transcript.split()) < 30:
                    continue
                summary = summarize_transcript(transcript)
                if custom_prompt:
                    story = generate_story_from_transcript(transcript, title, [custom_prompt] + themes)
                else:
                    story = generate_story_from_transcript(transcript, title, themes)
                with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                    f.write(f"Title: {title}
URL: {url}

")
                    f.write("Transcript:
" + transcript + "

")
                    f.write("Transcript Summary:
" + summary + "

")
                    f.write("Story:
" + story + "


")
                convert_story_to_audio(story, title)
    return OUTPUT_FILE


