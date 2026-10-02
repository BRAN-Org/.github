# Política de Segurança e Governança de Dados — BRAN Org

<p align="center">
  <a href="SECURITY.en.md"><img src="https://img.shields.io/badge/Read%20in-English-blue.svg?style=for-the-badge" alt="Read in English"></a>
</p>


A **BRAN Org** adota práticas rigorosas de segurança da informação, integridade de software e proteção de dados, alinhadas a padrões técnicos abertos e à legislação vigente.

---

## 1. Princípios de Governança e Integridade de Dados

Nossos acervos bibliométricos e bases de dados operam sob diretrizes formais de qualidade e reprodutibilidade:

- **FAIR Data Principles (Findable, Accessible, Interoperable, Reusable)**: Todos os dados são disponibilizados em formatos estruturados e abertos (`JSON`/`CSV`), com esquemas documentados, identificadores persistentes e metadados transparentes de proveniência.
- **Inviolabilidade da Origem (ISO 8000 / ISO/IEC 25012)**: Os dados espelham estritamente os registros públicos disponibilizados pelas fontes primárias. Nenhuma informação é inferida ou arbitrariamente completada sem documentação em logs de auditoria.
- **Integridade Criptográfica**: Cada versão de base e distribuição de pacote possui verificação por schemas canônicos e assinaturas/hashes de integridade.

---

## 2. Privacidade e Conformidade com a LGPD

O tratamento de metadados acadêmicos nos projetos da BRAN Org observa estritamente a **Lei Geral de Proteção de Dados (Lei nº 13.709/2018 - LGPD)**:

- **Escopo Exclusivo de Dados Públicos Acadêmicos**: Os repositórios tratam unicamente metadados bibliográficos de domínio público já tornados manifestamente públicos pelos autores e eventos científicos de origem (ex: nomes de autores para fins de atribuição científica, títulos, afiliações institucionais públicas e resumos), com fundamento nos arts. 7º, § 4º e 11, II, "c" da LGPD (atividades de pesquisa e ciência aberta).
- **Vedação de Dados Sensíveis**: É terminantemente proibido o armazenamento de dados pessoais sensíveis, documentos de identificação civil (como CPF ou RG), contatos privados (números de telefone particulares) ou credenciais.
- **Canal de Atendimento ao Titular**: Pesquisadores que desejem solicitar correções, atualizações de afiliação ou a exclusão de seus dados nos espelhos mantidos pela BRAN podem entrar em contato direto pelo canal: **`gabrielngama@gmail.com`**. As solicitações serão atendidas com prioridade.

---

## 3. Segurança de Código e Infraestrutura (ISO/IEC 27001)

- **Higiene de Credenciais**: É proibido o versionamento de tokens de API, segredos ou chaves privadas nos repositórios. Pipelines de CI realizam escaneamento automático de credenciais.
- **Proteção de Branches**: Repositórios centrais possuem proteção de branch na `main`, exigindo validação prévia de testes e aprovação técnica.

---

## 4. Relato Responsável de Vulnerabilidades (Responsible Disclosure)

Se você identificar uma falha de segurança, vulnerabilidade em ferramentas ou exposição indevida de dados em qualquer repositório da organização, solicitamos que **não abra uma Issue pública**.

Envie um relatório confidencial para:
 **[gabrielngama@gmail.com](mailto:gabrielngama@gmail.com)**

### O que incluir no relato:
1. Descrição clara e escopo da vulnerabilidade.
2. Passos reprodutíveis ou prova de conceito (PoC).
3. Avaliação de impacto potencial estimado.

Todas as comunicações serão tratadas com confidencialidade, agilidade na investigação e aplicação de correções.

