import gradio as gr
import os
from datetime import datetime

def get_latest_csv():
    """Get the path to the latest CSV file in the results directory."""
    results_dir = "results"
    csv_files = [f for f in os.listdir(results_dir) if f.endswith('.csv')]
    if not csv_files:
        return None
    latest_csv = max(csv_files, key=lambda x: os.path.getctime(os.path.join(results_dir, x)))
    return os.path.join(results_dir, latest_csv)

def create_ui():
    # Add download button with plain text labels
    download_btn = gr.File(
        label="Download Results CSV",
        file_count="single",
        type="file",
        interactive=False
    )
    
    def update_download_button():
        csv_path = get_latest_csv()
        if csv_path and os.path.exists(csv_path):
            return csv_path
        return None
    
    # Update download button whenever results are generated
    process_btn.click(
        fn=update_download_button,
        outputs=[download_btn],
        queue=False
    )
    
    # Create interface with plain text labels
    interface = gr.Interface(
        title="AI Prompt Analysis",
        description="Analyze and compare responses from different AI models",
        inputs=[
            gr.Textbox(label="Enter your prompt", placeholder="Type your prompt here..."),
            gr.Slider(label="Correlation Threshold", minimum=0.0, maximum=1.0, value=0.5, step=0.1),
            gr.Slider(label="Metric Weight", minimum=0.0, maximum=2.0, value=1.0, step=0.1)
        ],
        outputs=[
            gr.Dataframe(label="Results"),
            gr.Plot(label="Correlation Heatmap"),
            gr.Plot(label="Metrics Comparison"),
            gr.Plot(label="Radar Chart"),
            download_btn
        ],
        examples=[
            ["What is the capital of France?", 0.5, 1.0],
            ["Explain quantum computing", 0.5, 1.0],
            ["Write a short poem about AI", 0.5, 1.0]
        ],
        theme=gr.themes.Soft()
    )
    
    return interface

if __name__ == "__main__":
    # Create results directory if it doesn't exist
    os.makedirs("results", exist_ok=True)
    
    # Create and launch the UI
    interface = create_ui()
    interface.launch(share=False) 