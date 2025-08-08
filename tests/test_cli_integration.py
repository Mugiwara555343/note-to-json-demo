import subprocess
import pytest
import os
from pathlib import Path
import tempfile
import json


@pytest.mark.integration
def test_cli_integration():
    """Test that the note2json CLI works end-to-end"""
    # Get a demo file to test with
    demo_file = Path(__file__).parent.parent / "demo_entries" / "demo_entry.md"
    
    if not demo_file.exists():
        pytest.skip("Demo file not found")
    
    # Create a temporary output file
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp_file:
        tmp_json = Path(tmp_file.name)
    
    try:
        # Run the CLI command with UTF-8 environment
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        
        result = subprocess.run(
            ['note2json', str(demo_file), '-o', str(tmp_json)],
            capture_output=True,
            text=True,
            encoding='utf-8',
            env=env
        )
        
        # Assert the command succeeded
        assert result.returncode == 0, f"CLI failed with return code {result.returncode}. stderr: {result.stderr}"
        
        # Assert the output file was created
        assert tmp_json.exists(), f"Output file {tmp_json} was not created"
        
        # Optional: verify the JSON is valid
        import json
        with open(tmp_json, 'r') as f:
            data = json.load(f)
            assert "title" in data
            assert "timestamp" in data
            
    finally:
        # Clean up the temporary file
        if tmp_json.exists():
            tmp_json.unlink()


@pytest.mark.integration
def test_cli_stdout_flag():
    """Test that the --stdout flag works correctly"""
    # Get a demo file to test with
    demo_file = Path(__file__).parent.parent / "demo_entries" / "demo_entry.md"
    
    if not demo_file.exists():
        pytest.skip("Demo file not found")
    
    # Run the CLI command with --stdout flag
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    
    result = subprocess.run(
        ['note2json', str(demo_file), '--stdout'],
        capture_output=True,
        text=True,
        encoding='utf-8',
        env=env
    )
    
    # Assert the command succeeded with exit code 0
    assert result.returncode == 0, f"CLI failed with return code {result.returncode}. stderr: {result.stderr}"
    
    # Assert STDOUT contains valid JSON
    assert result.stdout.strip(), "STDOUT should not be empty"
    
    # Parse the JSON and verify it has the required fields
    try:
        data = json.loads(result.stdout.strip())
        assert "title" in data, "JSON should contain 'title' field"
        assert "timestamp" in data, "JSON should contain 'timestamp' field"
    except json.JSONDecodeError as e:
        pytest.fail(f"STDOUT should contain valid JSON: {e}")
