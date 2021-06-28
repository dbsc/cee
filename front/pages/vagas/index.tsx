import { GetServerSideProps } from 'next'
import Head from 'next/head'
import styles from '../../styles/vagas.module.scss'
import { getSession } from 'next-auth/client'
import { CardVaga } from '../../components/CardVaga'
import { DashBoardHeader } from '../../components/DashboardHeader'

import Array from '../../vacancies.json'

export default function Vagas({ session }) {
	const vagas = Array.map((vaga, index) => {
		return {
			id: index,
			title: vaga.title,
			company: vaga.company,
			field: vaga.field,
			position: vaga.position,
			pay: new Intl.NumberFormat('pr-BR', { style: 'currency', currency: 'BRL' }).format(vaga.pay),
			date: vaga.expiration_date,
		}
	})
	return (
		<>
			<Head>
				<title>Vagas | CEE</title>
			</Head>

			<DashBoardHeader />
			<div className={styles.container}>
				<div className={styles.content}>
					<h1 className={styles.title}>Vagas</h1>

					<div className={styles.cards}>
						{vagas.map((vaga) => (
							<CardVaga
								id={vaga.id}
								title={vaga.title}
								company={vaga.company}
								field={vaga.field}
								position={vaga.position}
								pay={vaga.pay}
								date={vaga.date}
							/>
						))}
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
