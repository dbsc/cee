import Head from 'next/head'

import styles from '../styles/index.module.scss'
export default function Home() {
	return (
		<>
			<Head>
				<title>Início | CEE</title>
			</Head>

			<div className={styles.container}>
				<img src="/images/aguia.svg" alt="Águia" />
			</div>
		</>
	)
}
