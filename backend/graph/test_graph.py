from graph import app

initial_state = {"question": "What is the governing law for the Tata contract?"}

print("Starting workflow...\n")
result = app.invoke(initial_state)

print("\n--- FINAL OUTPUT ---")
print(result["answer"])