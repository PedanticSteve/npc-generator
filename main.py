import npc_generator

def main():
    print("🔮 NPC Generator CLI")
    while True:
        print("\nSelect an option:")
        print("1️⃣ Generate a new NPC")
        print("2️⃣ Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            npc = npc_generator.generate_npc()
            print("\n🎭 **Generated NPC:**")
            for key, value in npc.items():
                print(f"➡️ {key}: {value}")

        elif choice == "2":
            print("🔮 Exiting NPC Generator. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
