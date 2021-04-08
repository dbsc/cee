import styles from './styles.module.scss'

export function Hero() {
	return (
		<div className={styles.container}>
			<div className={styles.content}>
				<img src="/logos/logo_white.svg" alt="CEE" />
				<p>
					A <span>CEE</span> é uma liga universitária que trabalha para conectar os alunos do ITA às
					melhores oportunidades do mercado de trabalho
				</p>
				<div className={styles.buttons}>
					<a href="/">Fazer Login</a>
					<a href="/">Divulgar vaga no ITA</a>
				</div>
			</div>
		</div>
	)
}
