# Day 17: Logger Text Processor App
import logging

logger = logging.getLogger("AppLogger")

class TextProcessor:
    def __init__(self, output_filepath):
        self.output_filepath = output_filepath

    def process_and_save(self, text):
        if not text:
            print("Warning: Received empty text")
            logger.warning("Empty string passed to processor")
            return
        
        processed = text.upper().strip()
        
        # Write to the configured path
        with open(self.output_filepath, "w") as f:
            f.write(processed)
            
        print(f"File saved: {self.output_filepath}")
        logger.info(f"Successfully processed {len(text)} characters")
