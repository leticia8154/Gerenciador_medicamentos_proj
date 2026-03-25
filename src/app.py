from core import validar_medicamento

def main():
    print("="*30)
    print("  CONTROLE DE MEDICAMENTOS v1.0.0  ")
    print("="*30)    
    nome = input("Nome do Medicamento: ")
    try:
        dose = float(input("Dose (mg): "))
        if validar_medicamento(nome, dose):
            print(f"\n✅ {nome} cadastrado com sucesso!")
    except ValueError as e:
        print(f"\n❌ Erro: {e}")
if __name__ == "__main__":
    main()
