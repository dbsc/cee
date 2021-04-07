import Head from 'next/head'
import styles from '../styles/quem-somos.module.scss'

export default function QuemSomos() {
	return (
		<>
			<Head>
				<title>Quem Somos | CEE</title>
			</Head>
			<div className={styles.container}>
				<h1>Quem Somos</h1>
			</div>
		</>
	)
}
