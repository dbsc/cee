import Head from 'next/head'

import styles from '../styles/index.module.scss'
export default function Home() {
	return (
		<>
			<Head>
				<title>Início | CEE</title>
			</Head>

			<div className={styles.container}>
				<h1>Projeto MTP</h1>
				<img src="/logo.png" alt="Logo CEE" />
			</div>
		</>
	)
}
