import styles from './styles.module.scss'

export function Servicos() {
	return (
		<div className={styles.container}>
			<h1 className={styles.title}>
				Nossos Serviços
			</h1>
			<div className={styles.content}>
				<h1 className={styles.Section}>Divulgação de Oportunidades</h1>
				<div className={styles.oportunidades}>
					<div className={styles.left}>
						<div className={`${styles.box} ${styles.a}`}>
							<h2>
								Palestras
							</h2>
							<p>
								Compartilhe sobre a empresa, seu dia-a-dia, sua cultura, oportunidades, 
								meios de entrada e dicas sobre o processo seletivo. Somado a um coffe-break 
								para que os alunos possam interagir mais ainda com os palestrantes e fazer 
								networking.
							</p>
						</div>
						<div className={`${styles.box} ${styles.b}`}>
							<h2>
								Hackathons
							</h2>
							<p>
								O ITA é um centro de excelência em tecnologia. As capacidades analíticas e o 
								interesse em empreendorismo tornam os iteanos ainda mais propensos a participar 
								dessa competição.
							</p>
						</div>
					</div>
					<div className={styles.right}>
						<div className={`${styles.box} ${styles.c}`}>
							<h2>
								Treinamentos / Workshops
							</h2>
							<p>
								Esse tipo de atividade foca em capacitar os alunos com habilidades necessárias 
								no mercado. São um excelente meio de apresentar a cultura, os valores da empresa 
								e como lida com o desenvolvimento dos seus colaboradores.
							</p>
						</div>
						<div className={`${styles.box} ${styles.d}`}>
							<h2>
								Diversos
							</h2>
							<p>
								Há ainda a possibilidade de disponibilizarmos espaço para a realização de etapas 
								de processos seletivos dentro do próprio Campus, ou até mesmo organizarmos idas a 
								SP para eventos, tudo ajudar a conectar sua empresa com o aluno do ITA.
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	)
}
