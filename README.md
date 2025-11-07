Script para monitorar os logs e enviar para o Discord via webhook

Este script lê o arquivo server.log do Minecraft (presente em praticamente todas as versões que testei, incluindo Beta, Alpha e MCPE) e envia atualizações dos logs em tempo real para um canal do Discord usando webhook.

Observações importantes:

Não é um plugin; funciona como um programa externo.

Não vai funcionar corretamente para servidores hospedados remotamente, sem acesso direto ao server.log.

É útil principalmente para servidores locais.

Funciona em versões antigas do Minecraft, incluindo a B1.0, que não possuem suporte nativo para enviar logs ao Discord.

Simples, mas útil.

Como usar:

Baixe os arquivos blocklogger.py e run_blocklogger.py.

Coloque-os na mesma pasta onde está o server.log ou informe o caminho completo do arquivo no script.

Copie o webhook do Discord e defina o canal para onde os logs serão enviados.

Execute run_blocklogger.py.

Caso não funcione, verifique:

Se o caminho do server.log está correto.

Se você instalou a biblioteca requests (necessária para enviar dados via HTTPS).

Você também pode rodar pelo terminal:
