import { GetServerSideProps } from 'next'
import { getSession } from 'next-auth/client'
import Head from 'next/head'
import { useRouter } from 'next/router'
import { DashBoardHeader } from '../../components/DashboardHeader'
import styles from '../../styles/vaga.module.scss'
import { FaCalendarAlt, FaMapMarkerAlt, FaRegMoneyBillAlt } from 'react-icons/fa'
import { StandartButton } from '../../components/StandartButton'

export default function Vaga() {
	const router = useRouter()
	return (
		<>
			<Head>
				<title>Vaga | CEE</title>
			</Head>
			<DashBoardHeader />
			<div className={styles.container}>
				<div className={styles.content}>
					<div className={styles.box}>
						<div className={styles.mainInfo}>
							<div className={styles.title}>Sales Account Intern</div>
							<div className={styles.subtitle}>Preparo</div>

							<div className={styles.info1}>
								<div>Área: </div>
								<div>Posição: </div>
							</div>

							<div className={styles.icons}>
								<div className={styles.icon}>
									<FaMapMarkerAlt />
									<div>Remoto</div>
								</div>
								<div className={styles.icon} id={styles.money}>
									<FaRegMoneyBillAlt />
									<div>R$ 1000,00</div>
								</div>
								<div className={styles.icon} id={styles.data}>
									<FaCalendarAlt />
									<div>
										Até <span> 10/10/2021</span>
									</div>
								</div>
							</div>

							<StandartButton>Candidar-se</StandartButton>

							<div>Essa é a vaga de id: {router.query.id}</div>
						</div>

						<div className={styles.description}>
							<div className={styles.title}>DESCRIÇÃO DA VAGA</div>
							<div className={styles.subtitle}>Sobre a Startup 🚀</div>
							<div>
								A Preparo é uma startup de tecnologia em recrutamento e seleção que conecta jovens
								de alto potencial ao emprego dos sonhos. Somente em 2020, a empresa foi responsável
								por colocar cerca de 500 pessoas no mercado, em mais de 100 empresas de pequeno,
								médio e grande porte. Tudo isso porque a Preparo usa a tecnologia para entregar às
								empresas candidatos com alta aderência aos cargos desejados.
							</div>
							<div className={styles.subtitle}>Sobre a vaga: 👩‍🚀</div>
							<div>
								O estágio de férias no área comercial da Preparo será um grande desafio para o
								estudante que sonha em construir uma carreira na área, aqui somos diariamente
								desafiados pensando sempre na melhoria contínua, individual e coletiva. Trabalhamos
								num ambiente colaborativo e é muito comum as áreas se envolverem em projetos de
								outras áreas. Inicialmente, suas responsabilidades serão: <br /> <br />
								◾ Desenvolver diferentes abordagens e formas de prospecção ativa, marcar e realizar
								reuniões de demonstração, fechar contratos e criar cases mais atrativos de
								apresentação do produto; <br />
								◾ Você deve contribuir para o aumento das vendas e manter nosso relacionamento
								empresa-cliente em um alto padrão; <br />
								◾ Estar em constante contato com o time de operação, entendendo a fundo como cada
								coisa funciona e alinhando cronogramas de entrega, de acordo com as necessidades de
								cada cliente. <br /> <br />
								Aqui na Preparo nossos valores sustentam o sonho de cooperar para um mundo com mais
								gente realizada. Todos os dias, eles movem cada um dos nossos colaboradores a darem
								o seu melhor. Estes são 5 princípios que estão intrínsecos em cada ação que tomamos
								como empresa: <br /> <br />
								1. Um pé no chão e outro na lua 🌖 Sonhamos alto para atingir nosso propósito, mas
								mantemos o pé no chão diariamente para não perder o foco. <br /> <br />
								2. O básico é nosso ponto de partida 📍 Não abrimos mão do que é essencial, mas
								acreditamos que a melhoria vem da execução, com aprendizado voltado ao sucesso.{' '}
								<br />
								<br />
								3. Nosso combustível é gente ⛽ Carregamos um profundo senso de compromisso em
								impactar vidas: de candidatos, recrutadores e do nosso time, o que nos leva a gerar
								valor por meio de relacionamentos. <br /> <br />
								4. Nossos astronautas são colaborativos 👨🏻‍🚀 A colaboração gera troca de conhecimento
								e dá voz às nossas pessoas, por isso estimulamos o trabalho em equipe e acreditamos
								no poder da complementaridade. <br /> <br />
								5. Nosso planeta é a Preparo 🌎 Somos os maiores embaixadores da nossa marca. Temos
								orgulho de fazer parte da Preparo e acreditamos que estamos construindo algo maior
								do que nós. OBS: Obs: Possibilidade formalizar um estágio regular após o estágio de
								férias. (de acordo com desempenho) 👀
							</div>
							<div className={styles.subtitle}>Cronograma 📆</div>
							29/06 - 1ª Fase: Inscrições e testes na plataforma da Preparo <br />
							01/07 - 2ª Fase: Entrevistas <br />
							05/07 - Início do estágio de férias
							<div className={styles.subtitle}>Requisitos</div>
							<div>
								Habilidades que são necessárias para a vaga 🛠️ <br />
								◾ Excelentes habilidades de comunicação e negociação; <br />
								◾ Compreensão de métricas de desempenho; <br />
								◾ Habilidades analíticas e de gerenciamento de tempo; <br />
								◾ Diferencial: já ter trabalhado com vendas e/ou atendimento ao cliente. <br />
							</div>
						</div>
					</div>

					<div className={styles.button}>
						<StandartButton>CANDIDATAR-SE</StandartButton>
					</div>
				</div>
			</div>
		</>
	)
}

export const getServerSideProps: GetServerSideProps = async (context) => {
	const session = await getSession(context)
	if (!session) {
		return {
			redirect: {
				destination: '/',
				permanent: false,
			},
		}
	}
	return {
		props: {
			session,
		},
	}
}
