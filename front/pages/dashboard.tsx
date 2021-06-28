import { GetServerSideProps } from 'next'
import Head from 'next/head'
import styles from '../styles/dashboard.module.scss'
import { getSession } from 'next-auth/client'
import { DashBoardHeader } from '../components/DashboardHeader'

export default function Vagas({ session }) {
	return (
		<>
			<Head>
				<title>Dashboard | CEE</title>
			</Head>
			<div className={styles.body}>
				<DashBoardHeader />

				<div className={styles.content}>
					<div className={styles.info}>
						<div>
							Bem vindo, <br />
							<span>{session.user.name}</span>
						</div>
						<div>
							<p>Acesse nossos Serviços</p>
							<div className={styles.buttons}>
								<a className={styles.button} href="/vagas">
									Vagas
								</a>
								<a className={styles.button} href="/">
									Eventos
								</a>
							</div>
						</div>
					</div>
					<img src="/images/aguia.svg" alt="Águia'" />
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
