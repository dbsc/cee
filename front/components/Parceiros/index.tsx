import styles from './styles.module.scss'

export function Parceiros() {
	return (
		<div className={styles.container}>
			<div className={styles.content}>
				<h1 className={styles.title}>
					Nossos <br />
					Parceiros
				</h1>
				<div className={styles.parceiros}>
					<img src="/parceiros/ITA.png" alt="logo ITA" />
					<img src="/parceiros/aeita.png" alt="logo AEITA" />
				</div>
			</div>
		</div>
	)
}
